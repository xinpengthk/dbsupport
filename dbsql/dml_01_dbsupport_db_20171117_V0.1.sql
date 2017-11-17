

use dbsupport_db;

insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('CREATE', 'databases, tables, or indexes', now(), now());
insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('DROP', 'databases, tables, or views', now(), now());
insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('GRANT OPTION', 'databases, tables, or stored routines', now(), now());
insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('LOCK TABLES', 'databases', now(), now());
insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('REFERENCES', 'databases or tables', now(), now());
insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('EVENT', 'databases', now(), now());
insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('ALTER', 'tables', now(), now());
insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('DELETE', 'tables', now(), now());
insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('INDEX', 'tables', now(), now());
insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('INSERT', 'tables or columns', now(), now());
insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('SELECT', 'tables or columns', now(), now());
insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('UPDATE', 'tables or columns', now(), now());
insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('CREATE TEMPORARY TABLES', 'tables', now(), now());
insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('TRIGGER', 'tables', now(), now());
insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('CREATE VIEW', 'views', now(), now());
insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('SHOW VIEW', 'views', now(), now());
insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('ALTER ROUTINE', 'stored routines', now(), now());
insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('CREATE ROUTINE', 'stored routines', now(), now());
insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('EXECUTE', 'stored routines', now(), now());
insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('FILE', 'file access on server host', now(), now());
insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('CREATE TABLESPACE', 'server administration', now(), now());
insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('CREATE USER', 'server administration', now(), now());
insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('PROCESS', 'server administration', now(), now());
insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('PROXY', 'server administration', now(), now());
insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('RELOAD', 'server administration', now(), now());
insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('REPLICATION CLIENT', 'server administration', now(), now());
insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('REPLICATION SLAVE', 'server administration', now(), now());
insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('SHOW DATABASES', 'server administration', now(), now());
insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('SHUTDOWN', 'server administration', now(), now());
insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('SUPER', 'server administration', now(), now());
insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('ALL [PRIVILEGES]', 'server administration', now(), now());
insert into cmdb_db_privs(priv_name, priv_desc, created_time, updated_time) values('USAGE', 'server administration', now(), now());
commit;
