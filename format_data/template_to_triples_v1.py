#!/usr/bin/python
# -*- coding: <encoding name> -*-

from __future__ import print_function
import xlrd
from xlrd.sheet import ctype_text
import rdflib
from rdflib import URIRef, Literal, Graph, Namespace


def template_to_triples(path):
    
    # Read file
    try:
        book = xlrd.open_workbook(path)
    except:
        print('File ' + path + ' does not exist.')
        exit()
    
    # Read worksheets
    sheet_exp = book.sheet_by_name('Experiment')
    sheet_plant = book.sheet_by_name('Plant')
    sheet_obs = book.sheet_by_name('Observation')

    experiments = list()
    plants = list()
    observations = list()
    
    for rowNum in range(3, sheet_exp.nrows):
        row = sheet_exp.row(rowNum)
        experiments.append({
            'exp_uri': row[1].value,
            'exp_id': row[2].value,
            'exp_year': str(int(row[3].value)),
            'exp_country': row[4].value
            })
            
    for rowNum in range(3, sheet_plant.nrows):
        row = sheet_plant.row(rowNum)
        plants.append({
            'exp_uri': row[1].value,
            'desc_uri': row[2].value,
            'desc_id': str(int(row[3].value)),
            'orig_uri': row[4].value,
            'orig_bioSt': row[5].value,
            'orig_id_uri': row[6].value,
            'id_ref_title': row[7].value,
            'id_ref_db': row[8].value
        })
            
    for rowNum in range(3, sheet_obs.nrows):
        row = sheet_obs.row(rowNum)
        observations.append({
            'exp_uri': row[1].value,
            'desc_uri': row[2].value,
            'obs_uri': row[3].value,
            'var_obj_uri': row[4].value,
            'var_uri': row[5].value,
            'var_label': row[6].value,
            'var_score': str(row[7].value)
        })
    
    
    # Create RDF graph
    g = Graph()
    rdf = Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
    dcterms = Namespace('http://purl.org/dc/terms/')
    obo = Namespace('http://purl.obolibrary.org/obo/')
    dbp = Namespace('http://dbpedia.org/property/')
    dbr = Namespace('http://dbpedia.org/resource/')
    sio = Namespace('http://semanticscience.org/resource/')
    to = Namespace('http://purl.obolibrary.org/obo/TO#')
    om = Namespace('http://def.seegrid.csiro.au/ontology/om/om-lite#')
    WUR_ont = Namespace('http://www.wur.nl/purl/ontology#')
    WUR_exp = Namespace('http://www.wur.nl/purl/experiment#')
    WUR_acc = Namespace('http://www.wur.nl/purl/accession#')
    WUR_obs = Namespace('http://www.wur.nl/purl/observation#')
    
    g.bind('rdf', rdf)
    g.bind('dcterms', dcterms)
    g.bind('obo', obo)
    g.bind('dbp', dbp)
    g.bind('dbr', dbr)
    g.bind('sio', sio)
    g.bind('to', to)
    g.bind('om', om)
    g.bind('WUR_ont', WUR_ont)
    g.bind('WUR_exp', WUR_exp)
    g.bind('WUR_acc', WUR_acc)
    g.bind('WUR_obs', WUR_obs)

    for e in experiments:
        g.add((URIRef(e['exp_uri']), rdf.type, obo.AGRO_00000370))
        g.add((URIRef(e['exp_uri']), dcterms.identifier, Literal(e['exp_id'])))
        g.add((URIRef(e['exp_uri']), dcterms.created, Literal(e['exp_year'])))
        g.add((URIRef(e['exp_uri']), dbp.location, 
        URIRef('http://dbpedia.org/resource/' + e['exp_country'])))
        
    for p in plants:
        g.add((URIRef(p['exp_uri']), obo.RO_0000057, URIRef(p['desc_uri'])))
        g.add((URIRef(p['desc_uri']), rdf.type, obo.PO_0000003))
        g.add((URIRef(p['desc_uri']), rdf.type, WUR_ont.descendant_plant))
        g.add((URIRef(p['desc_uri']), WUR_ont.descendant_of, URIRef(p['orig_uri'])))
        g.add((URIRef(p['desc_uri']), dcterms.identifier, Literal(p['desc_id'])))
        
        g.add((URIRef(p['orig_uri']), rdf.type, WUR_ont.original_plant))
        g.add((URIRef(p['orig_uri']), WUR_ont.has_id, URIRef(p['orig_id_uri'])))
        g.add((URIRef(p['orig_uri']), WUR_ont.has_biological_status, URIRef(p['orig_bioSt'])))
        
        g.add((URIRef(p['orig_id_uri']), rdf.type, WUR_ont.id))
        g.add((URIRef(p['orig_id_uri']), dcterms.title, Literal(p['id_ref_title'])))
        g.add((URIRef(p['orig_id_uri']), WUR_ont.stored_in, Literal(p['id_ref_db'])))
        
    for o in observations:
        g.add((URIRef(o['exp_uri']), sio.SIO_000219, URIRef(o['obs_uri'])))  # fix object
        
        g.add((URIRef(o['obs_uri']), rdf.type, om.observation))
        g.add((URIRef(o['obs_uri']), sio.SIO_000332, URIRef(o['desc_uri'])))
        g.add((URIRef(o['obs_uri']), to.has_phenotype_variable, URIRef(o['var_obj_uri'])))
        g.add((URIRef(o['obs_uri']), to.has_phenotype_score, Literal(o['var_score'])))
        
        g.add((URIRef(o['var_obj_uri']), rdf.type, URIRef(o['var_uri'])))
        g.add((URIRef(o['var_obj_uri']), dcterms.title, Literal(o['var_label'])))
    
    # print(experiments)
    # print(plants)
    # print(observations)
    
    # print(g.serialize(format='turtle'))
    g.serialize(destination='data.ttl', format='turtle')
    print('Done.')


if __name__ == '__main__':
    path = 'data_template_v1.xlsx'
    template_to_triples(path)
