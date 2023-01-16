package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

type album struct {
	ID     string  `json:"id"`
	Title  string  `json:"title"`
	Artist string  `json:"artist"`
	Price  float64 `json:"price"`
}

// albums slice records the album data (& replaces a persistent DB)
var albums = []album{
	{ID: "1", Title: "Blue Train", Artist: "John Coltrane", Price: 56.99},
	{ID: "2", Title: "Jeru", Artist: "Gerry Mulligan", Price: 17.99},
	{ID: "3", Title: "Sarah Vaughan and Clifford Brown", Artist: "Sarah Vaughan", Price: 39.99},
}

func main() {
	router := gin.Default()
	router.GET("/albums", getAlbums)
	router.GET("/albums/:id", getAlbumByID) // colon signifies path param
	router.POST("/albums", postAlbums)

	router.Run("localhost:8080")
}

// getAlbums serves the list of all albums as JSON
func getAlbums(c *gin.Context) {
	// gin.Context is the most important part of Gin.
	// It carries request details, validates and serializes JSON, and more.
	c.IndentedJSON(http.StatusOK, albums)
}

// Note: Replace Context.IndentedJSON with Context.JSON to send more compact JSON. In practice, the
//       indented form is much easier to work with when debugging and the size difference is usually small.

// postAlbum adds a new album provided as JSON to albums repo
func postAlbums(c *gin.Context) {
	var newAlbum album

	// BindJSON binds the received JSON to newAlbum
	if err := c.BindJSON(&newAlbum); err != nil {
		return
	}

	albums = append(albums, newAlbum)
	c.IndentedJSON(http.StatusCreated, newAlbum)
}

func getAlbumByID(c *gin.Context) {
	// Context.Param retrieves path parameters from the URL. A placeholder/key for the parameter is required in path
	id := c.Param("id")

	for _, album := range albums {
		if id == album.ID {
			c.IndentedJSON(http.StatusOK, album)
			return
		}
	}
	c.IndentedJSON(http.StatusNotFound, gin.H{"message": "album not found"})
}
