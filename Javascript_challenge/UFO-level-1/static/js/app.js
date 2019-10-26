// from data.js
var tableData = data;
let tablebody = d3.select("tbody");

// Event that Triggers a Function When the Button is Clicked
function handleClick(){
    // getting the value of the input date entered 
    let dateValue = d3.select("#datetime").property("value");
    let filteredData = tableData;
    // find the data based on the date entered
    if(dateValue) {
        filteredData = filteredData.filter((row) => row.datetime === dateValue);
    }
    printRows(filteredData);
}


//function that prints the data on the screen 
function printRows(data){
    //clear existing data
    tablebody.html("");
    data.forEach((dataRow) => {
        let rowinfo = tablebody.append("tr");
        // interate throught the values in the object
        Object.values(dataRow).forEach((value) => {
            let data = rowinfo.append("td");
            data.text(value);
        });
    })
}

// what happens when you click filter button
d3.selectAll("#filter-btn").on("click", handleClick);
printData(tableData);