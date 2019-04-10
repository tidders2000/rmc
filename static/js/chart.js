
queue()
    .defer(d3.json, "/data")
    .await(makeGraphs);
    
function makeGraphs(error, dataData) {

    console.log(dataData)
}