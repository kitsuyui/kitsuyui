# RDAP

## 使い方

```
$ curl https://rdap.apnic.net/ip/0.0.0.0
{
  "errorCode" : 404,
  "title" : "Not Found",
  "description" : [ "The server has not found anything matching the Request-URI." ],
  "rdapConformance" : [ "rdap_level_0" ],
  "notices" : [ {
    "title" : "Terms and Conditions",
    "description" : [ "This is the APNIC WHOIS Database query service. The objects are in RDAP format." ],
    "links" : [ {
      "value" : "https://rdap.apnic.net/ip/0.0.0.0",
      "rel" : "terms-of-service",
      "href" : "http://www.apnic.net/db/dbcopyright.html",
      "type" : "text/html"
    } ]
  } ]
}
```

## RFC 7482

https://tools.ietf.org/html/rfc7482
