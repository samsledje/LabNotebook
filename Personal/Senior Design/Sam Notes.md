# Sam Notes

Questions for Wan-Ping

- Start from CNV, go into browser, click on genes known in that area,

Show first 10/15 genes, link where you can see the full list

More SQL → select * from Annotation WHERE pathogen = 'Pathogenic' AND support LIKE 'criteria provided%';

Connect to MariaDB: sudo /usr/bin/mysql -u root -p

```r
library(RMariaDB)
con <- dbConnect(MariaDB(),host='localhost',username='jax-cnv',password='JAX',dbname='CNV_INFORMATION')
rs <- dbSendQuery(con, 'SELECT * FROM Variation')
res <- dbFetch(rs, n=-1)
```

Define all columns as factors so you can sort by all of them

Things to fix in release:

- Improve loading user experience
- Update Help/About to have actual help instead of the just the abstract