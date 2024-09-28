def google_api(data):
    site = "".join(data['site'].strip().split(" "))
    if(site==""):
        return "主域名不能为空"
    file = data['filetype'].strip().split(" ")
    a = data['inurl'].strip().split(" ")
    b = data['intitle'].strip().split(" ")
    c = data['intext'].strip().split(" ")

    def infiletype(types):
      for i,v in enumerate(types):
         types[i] = "filetype:"+v
      return types
   
   
    def inurl(urls):
      for i,v in enumerate(urls):
        urls[i] = "inurl:\""+v+"\""
      return urls

    def intitle(titles):
      for i,v in enumerate(titles):
        titles[i] = "intitle:\""+v+"\""
      return titles

    def intext(texts):
      for i,v in enumerate(texts):
        texts[i] = "intext:\""+v+"\""
      return texts
        
    def max(urls,titles,texts,filetypes):
      OR = " OR "
      f = OR.join(filetypes)
      u = OR.join(urls)
      ti = OR.join(titles)
      te = OR.join(texts)
      if(f!="filetype:"):
         f+=" "
      else:
         f=""
      if(u!="inurl:\"\""):
         u+=" OR "
      else:
           u=""
      if(ti!="intitle:\"\""):
         ti+=" OR "
      else:
         ti=""
       #return "site:"+site+" "+f+u+ti+te
      return f"site:{site} {f}{u}{ti}{te}"

    return ((max(inurl(a),intitle(b),intext(c),infiletype(file))))

    