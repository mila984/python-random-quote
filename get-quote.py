def primary():
  pyton3 get-quote.py

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes [0])

if __name__== "__main__"
+ main()
