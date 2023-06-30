const mongoose = require("mongoose");
const SensorData = new mongoose.Schema({
    Temp : {
        type : Number,
        required: true
    }
},{
    timestamps: true
});

module.exports = mongoose.model("SensorData",SensorData);