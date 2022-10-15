package calendar

import "errors"

type Date struct {
	year  int
	month int
	day   int
}

func (date *Date) SetYear(y int) error {
	if y < 0 {
		return errors.New("year must be greater than 0")
	}
	date.year = y
	return nil
}

func (date *Date) SetMonth(m int) error {
	if m < 1 || m > 12 {
		return errors.New("month must be an integer between 1 and 12")
	}
	date.month = m
	return nil
}

func (date *Date) SetDay(d int) error {
	if d < 1 || d > 31 {
		return errors.New("day must be an integer between 1 and 31")
	}
	date.day = d
	return nil
}

func (date *Date) SetDate(y, m, d int) error {
	if err := date.SetYear(y); err != nil {
		return err
	}
	if err := date.SetMonth(m); err != nil {
		return err
	}
	if err := date.SetDay(d); err != nil {
		return err
	}
	return nil
}

func (date *Date) Year() int {
	return date.year
}

func (date *Date) Month() int {
	return date.month
}

func (date *Date) Day() int {
	return date.day
}
