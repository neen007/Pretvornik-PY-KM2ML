#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "Pozdrav! Ovo je program koji pretvara kilometre u milje!"

while True:
    print "Molim Vas upišite broj kilometara koji želite pretvoriti u milje:"
    km = raw_input("Kilometara: ")

    try:
        km = float(km.replace(",", "."))
        miles = km * 0.621371

        print "{0} kilometara je {1} milja.".format(km, miles)
    except Exception as e:
        print "Molim Vas upišite broj, a ne tekst! Hvala!"

    choice = raw_input("Da li želite ponovno pretvoriti kilometre u milje? (d/n): ")

    if choice.lower() != "d":
        break