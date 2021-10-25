\c ezbook

create user customer with nosuperuser;
grant connect on database "ezbook" to customer;
grant select on BestSellers to customer;
grant select on Bills to customer;
grant select on Cart to customer;
grant update on Cart to customer;

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