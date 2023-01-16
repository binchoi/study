package main

import (
	"html/template"
	"log"
	"net/http"
	"os"
	"regexp"
)

type Page struct {
	Title string
	Body  []byte // a byte slice, not string (type expected by our io libraries)
}

// save takes care of persistent storage
func (p *Page) save() error {
	filename := p.Title + ".txt"
	// permission 0600: file should be created with read-write permissions for the current user only
	return os.WriteFile(filename, p.Body, 0600)
}

func loadPage(title string) (*Page, error) {
	filename := title + ".txt"
	body, err := os.ReadFile(filename)
	if err != nil {
		return nil, err
	}
	return &Page{Title: title, Body: body}, nil
}

func viewHandler(w http.ResponseWriter, r *http.Request, title string) {
	p, err := loadPage(title)
	if err != nil {
		http.Redirect(w, r, "/edit/"+title, http.StatusFound)
		return
	}
	renderTemplate(w, "view", p)
}

func editHandler(w http.ResponseWriter, r *http.Request, title string) {
	p, err := loadPage(title)
	if err != nil {
		p = &Page{Title: title}
	}
	renderTemplate(w, "edit", p)
}

func saveHandler(w http.ResponseWriter, r *http.Request, title string) {
	body := r.FormValue("body")
	p := &Page{Title: title, Body: []byte(body)}
	err := p.save()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	http.Redirect(w, r, "/view/"+title, http.StatusFound)
}

// use http/template [native support by Go]
// template.Must wrapper causes panic when non-nil err returned
var templates = template.Must(template.ParseFiles("edit.html", "view.html"))

func renderTemplate(w http.ResponseWriter, tmpl string, p *Page) {
	err := templates.ExecuteTemplate(w, tmpl+".html", p)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError) // sends error message and specified response code
	}
}

// MustCompile differs from Compile in that it will panic if the expression compilation fails, while Compilation
// returns an error as a second parameter
var validPath = regexp.MustCompile("^/(edit|save|view)/([a-zA-Z0-9]+)$")

func makeHandler(fn func(http.ResponseWriter, *http.Request, string)) http.HandlerFunc {
	// the returned function is called a closure because it encloses values defined outside it
	// variable fn is enclosed by the closure
	return func(w http.ResponseWriter, r *http.Request) {
		m := validPath.FindStringSubmatch(r.URL.Path)
		if m == nil {
			http.NotFound(w, r) // write 404 Not Found error to the HTTP connection
			return              // return error to handler
		}
		fn(w, r, m[2]) // the title is the second subexpression (e.g. "/edit/title" -> ["/edit/title", "edit", "title"])
	}
}

func main() {
	http.HandleFunc("/view/", makeHandler(viewHandler)) // handle all requests to web root ("/view/") with handler
	http.HandleFunc("/edit/", makeHandler(editHandler)) // handle all requests to web root ("/edit/") with handler
	http.HandleFunc("/save/", makeHandler(saveHandler)) // handle all requests to web root ("/save/") with handler

	log.Println("Server started at http://localhost:8080/")
	log.Fatal(http.ListenAndServe(":8080", nil)) // listen on port 8080 on any interface
}
