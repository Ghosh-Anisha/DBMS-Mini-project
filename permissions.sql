\c ezbook

create user cust with nosuperuser;
grant connect on database "ezbook" to cust;
grant select on BestSellers to cust;
grant select on Bills to cust;
grant select on Cart to cust;
grant update on Cart to cust;

create user cashier with nosuperuser;
grant connect on database "ezbook" to cashier;
grant select on countbooks to cashier;
grant select on bills to cashier;
grant update on bills to cashier;
grant select on cart to cashier;

create user admin with nosuperuser;
grant connect on database "ezbook" to admin;
grant select on countbooks to admin;
grant update on countbooks to admin;
grant update on bestsellers to admin;
grant delete on bestsellers to admin;
grant select on bestsellers to admin;
grant delete on bills to admin;
grant select on bills to admin;
grant update on bills to admin;
grant select on cart to admin;
grant delete on cart to admin;

grant select on customer to admin;
grant delete on customer to admin;
grant update on customer to admin;
grant select on customer to cust;
grant update on customer to cust;

grant select on buys to admin;

grant select on customerfeedback to admin;
grant select on customerfeedback to cust;
grant update on customerfeedback to cust;
grant delete on customerfeedback to cust;

grant select on books to admin;
grant update on books to admin;
grant delete on books to admin;
grant select on books to cust;

grant select on produces to admin;
grant update on produces to admin;
grant delete on produces to admin;

grant select on PublicationHouse to admin;
grant update on PublicationHouse to admin;
grant delete on PublicationHouse to admin; 
grant select on PublicationHouse to cust;

grant select on RequestForBooks to admin;
grant delete on RequestForBooks to admin;
grant select on RequestForBooks to cust;
grant update on RequestForBooks to cust;

