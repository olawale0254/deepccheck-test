CREATE TABLE interactions (
    id SERIAL PRIMARY KEY,
    input TEXT NOT NULL,
    output TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE metrics (
    id SERIAL PRIMARY KEY,
    interaction_id INTEGER REFERENCES interactions(id),
    metric_name TEXT NOT NULL,
    input_value FLOAT,
    output_value FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE alerts (
    id SERIAL PRIMARY KEY,
    interaction_id INTEGER REFERENCES interactions(id),
    metric_name TEXT NOT NULL,
    element TEXT NOT NULL,
    alert_type TEXT NOT NULL,
    value FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
