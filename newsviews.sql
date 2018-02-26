create view sluglog as
   select replace(path, '/article/', '') as slug, status, method, "time", id
   from log where path like '/article/%';

create view badsrch as
   select date_trunc('day', time) as srchbaddt, count(status) as badcnt
   from log
   where status != '200 OK'
   group by srchbaddt;

create view dailylogcnt as
   select date_trunc('day', time) as totdt, count(id) as logcnt
   from log
   group by date_trunc('day', time);