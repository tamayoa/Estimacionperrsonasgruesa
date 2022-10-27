A Continuación se encuentra la ruta en git del código :
https://github.com/tamayoa/Estimacionperrsonasgruesa/blob/main/macs.html

\subsection{macs.js}
\begin{verbatim}
var csvData = [];
const currentDate = new Date();
const timestamp = currentDate.getTime();

function nada (){

const Url = 'https://l3vy609ku1.execute-api.us-east-1.amazonaws.com/dev/reportes'
const Data = {
};

var date = document.getElementById("fecha").value;

//parameters
Parameters = {
    headers:{
        "Content-Type": "application/json; charset=UTF-8"
    },
    
    
     method:"GET"
};

fetch(Url, Parameters)
    .then(response => response.json())
    .then(data => { createTable(data)}) 


    function createTable(data){
        let tab = `<thead>
                <tr>
                    <th>TimeStamp</th>
                    <th>Data</th>
                    <th>Management</th>
                    <th>Persons</th>
                    <th>PPD</th>
                    <th>PPM</th>
                    <th>Total</th>
                </tr>
                    </thead>`;
         for(let i = 0; i < data.macs.length; i++){
            if (data.macs[i].time.includes(date)){
                if (data.macs[i].Total === undefined) {
                    var total = ' ';
                } else{
                    total = data.macs[i].Total
                }
                csvData[i] = [
                    data.macs[i].time.toString(),
                    data.macs[i].Data.toString(),
                    data.macs[i].Management.toString(),
                    data.macs[i].Personas.toString(),
                    data.macs[i].PPM.toString(),
                    total,
                    data.macs[i].PPD.toString(),
                    
            ];
                tab += `<tbody>
                <tr>
                <td>${data.macs[i].time}</td>
                <td>${data.macs[i].Data}</td>
                <td>${data.macs[i].Management}</td>
                <td>${data.macs[i].Personas}</td>
                <td>${data.macs[i].PPD}</td>
                <td>${data.macs[i].PPM}</td>
                <td>${total}</td>
                </tr>
                </tbody>`;
            }
             
        }
    
    
        
        document.getElementById("tabla").innerHTML = tab
    
       }
    


}

 
// CSV Function 
 function download_csv_file() {  

    if (csvData.length === 0) { 
        alert("Generate the data you want to download first");
    } else {
        var csv = " Time; Data; Managment; Personas; PPM; Total; PPD; \n" ;   
        
      
     csvData.forEach(function(row) {  
             csv += row.join(';');  

     });  
    
     var hiddenElement = document.createElement('a');  
     hiddenElement.href = 'data:text/csv;charset=utf-8,' + encodeURI(csv);  
     hiddenElement.target = '_blank';  
       
      
     hiddenElement.download = 'Macs' + '.csv';  
     hiddenElement.click();  
    }
    
    
    
 } 
