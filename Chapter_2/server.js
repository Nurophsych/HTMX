import express from 'express';

const app = express();

// Set static folder
app.use(express.static('public'));

// Parse URL-encoded bodies (as sent by HTML forms)
app.use(express.urlencoded({ extended: true }));

// Parse JSON bodies (as sent by API clients)
app.use(express.json());

// Handle GET request to fetch users (this should return something)
app.get('/users', async (req, res) => {
    res.json({ message: "User data will be here" }); // Example response
});

// Handle POST request for BMI calculation
app.post('/calculate', (req, res) => {
    const height = parseFloat(req.body.height);
    const weight = parseFloat(req.body.weight);

    if (!height || !weight) {
        return res.status(400).send('<p>Please provide valid height and weight.</p>');
    }

    const bmi = weight / (height * height);

    res.send(`
        <p>Height of ${height}m & Weight of ${weight}kg gives you a BMI of ${bmi.toFixed(2)}</p>
    `);
});

// Start server
app.listen(3000, () => {
    console.log('Server listening on port 3000');
});
