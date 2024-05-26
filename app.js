const express = require('express')
const shortId = require('shortid')

const app = express()

app.use(express.urlencoded({ extended: false }));

const database = [{"url": "https://www.google.com", "short": "aaaaa"}, {"url": "https://www.yahoo.com", "short": "bbbbb"}]

app.get('/',  (req, res) => {
    res.send("Hello World")
})
  
app.post('/shortUrls',  (req, res) => {
    var obj = {"url": req.body.url, "short": shortId.generate()};
    database.push(obj)
    console.log(obj);
    res.send(obj);

    res.redirect('/')
})
  
app.get('/:shortUrl', (req, res) => {
    const key1 = req.params.shortUrl;
    database.forEach(element => {
        const key2 = element.short;
        if (key1 === key2) { 
            console.log(element.url);
            res.redirect(element.url)
        }
    });
    res.redirect('/')
})


app.listen(5000);