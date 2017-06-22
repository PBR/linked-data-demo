var SPARQL_ENDPOINT = 'http://localhost:8890/sparql?default-graph-uri=http://localhost:8890/DAV/home/demo_user/rdf_sink&query='

var TEMPLATE_QUERIES = {
        1 : {
                text : '[working] Get number of accessions  with a specific phenotype',
                variables: ['phenotypeVariable', 'phenotypeValue'],
                query : readFile('sparqlQueries/template1.sparql', 'text')

            },
       2 : {
                text : '[working] Get number of accessions from a specific country of origin',
                variables: ['country'],
                query : readFile('sparqlQueries/template2.sparql', 'text')

           },
	3 : {
	  text : '[working] Get number of accessions with a specific phenotype from specific country of origin',
                variables: ['phenotypeVariable', 'phenotypeValue', 'country'],
                query : readFile('sparqlQueries/template3.sparql', 'text')

            },
        4 : {
                text : '[working] Get number of accessions with a specific biological status',
                variables: ['biologicalStatus'],
                query : readFile('sparqlQueries/template4.sparql', 'text')
            },

        5 : {
                text : '[?] Get number of accessions with a specific phenotype (from a certain environment: region or specific plant management)',
                variables: ['country'],
                query : readFile('sparqlQueries/template2.sparql', 'text')
            }
    };

var VARIABLE_QUERIES = {
        phenotypeVariable: readFile('sparqlQueries/getPhenotypeVariables.sparql', 'text'),
        phenotypeValue: readFile('sparqlQueries/getPhenotypeValues.sparql', 'text'),
        breakpoint: readFile('sparqlQueries/getBreakpoints.sparql', 'text'),
        country: readFile('sparqlQueries/getCountries.sparql', 'text'),
        biologicalStatus: readFile('sparqlQueries/getBiologicalStatus.sparql', 'text')
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
            alert(errorMsg);
            console.log(errorMsg)
        }
    });
    return content;
}


