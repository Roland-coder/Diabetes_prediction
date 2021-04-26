

function onClickedPredictDiabetes() {
    console.log("document loading");
    var pregnancy = document.getElementById("uipreg").value;
    var glucose = document.getElementById("uiglu").value;
    var bloodpressure = document.getElementById("uiblood").value;
    var skinthickness = document.getElementById("uithick").value;
    var insulin = document.getElementById("uiinsu").value;
    var bmi = document.getElementById("uibmi").value;
    var pedigree = document.getElementById("uiped").value;
    var age = document.getElementById("uiage").value;
    var diabetesvalue = document.getElementById("uiPredictDiabetes");
    var url = "http://127.0.0.1:5000/predict_diabetes";

    console.log(pregnancy);
    $.post(url, {
        pregnancies: pregnancy, 
        glucose: glucose, 
        bloodpressure: bloodpressure, 
        skinthickness: skinthickness, 
        insulin: insulin,
        bmi: parseFloat(bmi),
        diabetespedigreefunction: parseFloat(pedigree),
        age: age
    }, function(data, status) {
        console.log(data.get_diabetes);
        if(data.get_diabetes == 1.0) {
            diabetesvalue.innerHTML = "<h2>" + "has diabetes";
            console.log(status)
        } else {
            diabetesvalue.innerHTML = "<h2>" + "Does not have diabetes";
            console.log(status)
        }
    }
    
    );
}