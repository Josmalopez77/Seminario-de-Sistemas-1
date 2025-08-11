const express = require('express');
const app = express();
const port = 3000;

// Endpoint 1: /check
app.get('/check', (req, res) => {
    res.send("OK");
});

// Endpoint 2: /info
app.get('/info', (req, res) => {
    res.json({
        "Instancia": "Maquina 2 - Api 2",
        "Curso": "Seminario De Sistemas 1 A",
        "Grupo": "Grupo 7"
    });
});

app.listen(port, () => {
    console.log(`API corriendo en http://localhost:${port}`);
});
