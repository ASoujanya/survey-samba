CREATE TABLE client (
    id SERIAL,
    name TEXT
);

ALTER TABLE client ADD CONSTRAINT pk_client PRIMARY KEY(id);

CREATE TABLE client_location (
    id SERIAL,
    name TEXT,
    internal_id INT,
    client_id INT
)

ALTER TABLE client_location ADD CONSTRAINT pk_client_location PRIMARY KEY(id);

ALTER TABLE client_location ADD CONSTRAINT fk_loc_id_client_id FOREIGN KEY (client_id) REFERENCES client(id);

