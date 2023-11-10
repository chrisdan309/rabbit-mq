const { Client } = require('pg');

const client = new Client({
  user: 'nombre_de_usuario',
  host: 'localhost',
  database: 'nombre_de_la_base_de_datos',
  password: 'contraseña',
  port: 5432,
});

client.connect((err) => {
  if (err) {
    console.error('Error al conectarse a la base de datos', err.stack);
  } else {
    console.log('Conexión exitosa a la base de datos');
  }
});
