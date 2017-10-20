// var SPARQL_ENDPOINT = 'http://localhost:8890/sparql?query='
//var SPARQL_ENDPOINT = 'http://192.168.1.106/ld-relay/makeQuery?'
var SPARQL_ENDPOINT = 'http://plantbreeding.wur.nl/ld-relay/makeQuery?'


var TEMPLATE_QUERIES = {
        1 : {
                text : 'Get number of accessions  with a specific phenotype',
                variables: ['phenotypeVariable', 'phenotypeValue'],
                // query : readFile('sparqlQueries/template1.sparql', 'text'),
                queryGet : 'qID=1&pVar=#phenotypeVariable#&pVal=#phenotypeValue#'
            },
        2 : {
                text : 'Get accessions  with a specific phenotype',
                variables: ['phenotypeVariable', 'phenotypeValue'],
                // query : readFile('sparqlQueries/template2.sparql', 'text'),
                queryGet : 'qID=2&pVar=#phenotypeVariable#&pVal=#phenotypeValue#'
            },

       3 : {
                text : 'Get number of accessions from a specific country of origin',
                variables: ['country'],
                // query : readFile('sparqlQueries/template3.sparql', 'text'),
                queryGet : 'qID=3&country=#country#'
            },
       4 : {
                text : 'Get accessions from a specific country of origin',
                variables: ['country'],
                // query : readFile('sparqlQueries/template4.sparql', 'text'),
                queryGet : 'qID=4&country=#country#'
            },
       5 : {
                text : 'Get number of accessions with a specific phenotype from specific country of origin',
                variables: ['phenotypeVariable', 'phenotypeValue', 'country'],
                // query : readFile('sparqlQueries/template5.sparql', 'text'),
                queryGet : 'qID=5&pVar=#phenotypeVariable#&pVal=#phenotypeValue#&country=#country#'
            },
       6 : {
                text : 'Get accessions with a specific phenotype from specific country of origin',
                variables: ['phenotypeVariable', 'phenotypeValue', 'country'],
                // query : readFile('sparqlQueries/template6.sparql', 'text'),
                queryGet : 'qID=6&pVar=#phenotypeVariable#&pVal=#phenotypeValue#&country=#country#'
            },
        7 : {
                text : 'Get number of accessions with a specific biological status',
                variables: ['biologicalStatus'],
                // query : readFile('sparqlQueries/template7.sparql', 'text'),
                queryGet : 'qID=7&bioStat=#biologicalStatus#'
            },
        8 : {
                text : 'Get accessions with a specific biological status',
                variables: ['biologicalStatus'],
                // query : readFile('sparqlQueries/template8.sparql', 'text'),
                queryGet : 'qID=8&bioStat=#biologicalStatus#'
            },
        /*9 : {
                text : 'Get number of accessions with a specific phenotype (from a certain environment: region or specific plant management)',
                variables: ['country'],
                query : readFile('sparqlQueries/template2.sparql', 'text')
            } */
    };

/*
    var VARIABLE_QUERIES = {
        phenotypeVariable: readFile('sparqlQueries/getPhenotypeVariables.sparql', 'text'),
        phenotypeValue: readFile('sparqlQueries/getPhenotypeValues.sparql', 'text'),
        // breakpoint: readFile('sparqlQueries/getBreakpoints.sparql', 'text'),
        country: readFile('sparqlQueries/getCountries.sparql', 'text'),
        biologicalStatus: readFile('sparqlQueries/getBiologicalStatus.sparql', 'text')
} */

var VARIABLE_QUERY_IDs = {
        phenotypeVariable: 'gVar',
        phenotypeValue: 'gVal',
        // breakpoint: readFile('sparqlQueries/getBreakpoints.sparql', 'text'),
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


