var SPARQL_ENDPOINT = 'http://localhost:5011/makeQuery?'

var TEMPLATE_QUERIES = {
        1 : {
                text : 'Get number of accessions  with a specific phenotype',
                variables: ['phenotypeVariable', 'phenotypeValue'],
                queryGet : 'qID=1&pVar=#phenotypeVariable#&pVal=#phenotypeValue#'
            },
        2 : {
                text : 'Get accessions  with a specific phenotype',
                variables: ['phenotypeVariable', 'phenotypeValue'],
                queryGet : 'qID=2&pVar=#phenotypeVariable#&pVal=#phenotypeValue#'
            },

       3 : {
                text : 'Get number of accessions from a specific country of origin',
                variables: ['country'],
                queryGet : 'qID=3&country=#country#'
            },
       4 : {
                text : 'Get accessions from a specific country of origin',
                variables: ['country'],
                queryGet : 'qID=4&country=#country#'
            },
       5 : {
                text : 'Get number of accessions with a specific phenotype from specific country of origin',
                variables: ['phenotypeVariable', 'phenotypeValue', 'country'],
                queryGet : 'qID=5&pVar=#phenotypeVariable#&pVal=#phenotypeValue#&country=#country#'
            },
       6 : {
                text : 'Get accessions with a specific phenotype from specific country of origin',
                variables: ['phenotypeVariable', 'phenotypeValue', 'country'],
                queryGet : 'qID=6&pVar=#phenotypeVariable#&pVal=#phenotypeValue#&country=#country#'
            },
        7 : {
                text : 'Get number of accessions with a specific biological status',
                variables: ['biologicalStatus'],
                queryGet : 'qID=7&bioStat=#biologicalStatus#'
            },
        8 : {
                text : 'Get accessions with a specific biological status',
                variables: ['biologicalStatus'],
                queryGet : 'qID=8&bioStat=#biologicalStatus#'
            }
    };

var VARIABLE_QUERY_IDs = {
        phenotypeVariable: 'gVar',
        phenotypeValue: 'gVal',
        country: 'gC',
        biologicalStatus: 'gBS'
}

function readFile(url, dataType) {
    var content = null;
    $.ajax({
        url: url,
        async: false,
        cache: false,
        dataType: dataType,
        success: function(response) {
            content = response;
            console.log("Content of the file < " + url +"> has been read successfully.")
        },
        error: function(xhr){
            var errorMsg = ("Error reading file : " + xhr.status + " " +
                    xhr.statusText);
            // alert(errorMsg);
            console.log(errorMsg);
        }
    });
    return content;
}


