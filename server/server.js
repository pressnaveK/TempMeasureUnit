const express = require("express");
const mongoose = require("mongoose");
const bodyParser = require("body-parser");
const PORT = 3001;
const app = express();

const cors = require("cors");
app.use(express.json());
app.use(
  cors()
);
/*
app.post("/SensorData",(req,res)=>{
    console.log(req.body.Temp);
    res.send("Received");

});
*/

const SensorData = require("./model/SensorData");

mongoose
  .connect("mongodb://localhost:27017/HeatUnit", {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => {
    console.log("Connected Successfully");
    app.post("/SensorData", async (req, res) => {
        const Temp = req.body.Temp;
        
        
        const Data = new SensorData({
            Temp : Temp
        });
        await Data.save();
        console.log(Data);
        res.send("Value Inserted Sucessfully..")

        


    });

    app.listen(PORT, () => {
      console.log(`Server is listening on port ${PORT}`);
    });
  })
  .catch((error) => {
    console.error("Error connecting to MongoDB:", error);
  });
/*

app.listen(PORT, () => {
    console.log(`Server is listening on port ${PORT}`);
  });

  */