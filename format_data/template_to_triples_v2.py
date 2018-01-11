#!/usr/bin/python
# -*- coding: <encoding name> -*-

from __future__ import print_function
import xlrd
from xlrd.sheet import ctype_text
import rdflib
from rdflib import URIRef, Literal, Graph, Namespace, XSD


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
    
    for rowNum in range(4, sheet_exp.nrows):
        row = sheet_exp.row(rowNum)
        experiments.append({
            'exp_uri': row[1].value,
            'exp_id': row[2].value,
            'exp_year': str(int(row[3].value)),
            'exp_country': row[4].value
            })
            
    for rowNum in range(4, sheet_plant.nrows):
        row = sheet_plant.row(rowNum)
        #for idx, i in enumerate(row): print (idx, i)

        plants.append({
            'exp_uri': row[1].value,
            'desc_uri': row[2].value,
            'desc_id': str(int(row[3].value)),
            'orig_uri': row[4].value,
            'mcpd_accename': row[5].value,
            'mcpd_accenumb': row[6].value,
            'mcpd_donornumb': row[7].value,
            'mcpd_collnumb': row[8].value,
            'mcpd_othernumb': row[9].value,
            'orig_id_uri': row[10].value,
            'id_ref_title': row[11].value,
            'id_ref_db': row[12].value,
            'mcpd_cropname': row[13].value,
            'mcpd_genus': row[14].value,
            'mcpd_species': row[15].value,
            'mcpd_spauthor': row[16].value,
            'mcpd_subtaxa': row[17].value,
            'mcpd_subtauthor': row[18].value,
            'mcpd_sampstat': row[19].value, # aka 'orig_bioSt'
            'mcpd_mlsstat': row[20].value,
            'mcpd_storage': row[21].value,
            'mcpd_instcode': row[22].value,
            'mcpd_bredcode': row[23].value,
            'mcpd_bredname': row[24].value,
            'mcpd_collcode': row[25].value,
            'mcpd_collname': row[26].value,
            'mcpd_collinstaddress': row[27].value,
            'mcpd_collmissid': row[28].value,
            'mcpd_donorcode': row[29].value,
            'mcpd_donorname': row[30].value,
            'mcpd_duplsite': row[31].value,
            'mcpd_duplinstname': row[32].value,
            'mcpd_ancest': row[33].value,
            'mcpd_collsrc': row[34].value,
            'mcpd_coorddatum': row[35].value,
            'mcpd_coorduncert': row[36].value,
            'mcpd_origcty': row[37].value,
            'mcpd_collsite': row[38].value,
            'mcpd_elevation': row[39].value,
            'mcpd_georemeth': row[40].value,
            'mcpd_declatitude': row[41].value,
            'mcpd_latitude': row[42].value,
            'mcpd_declongitude': row[43].value,
            'mcpd_longitude': row[44].value,
            'mcpd_acqdate': row[45].value,
            'mcpd_colldate': row[46].value,
            'mcpd_remarks': row[47].value
        })
            
    for rowNum in range(4, sheet_obs.nrows):
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
    co = Namespace('http://www.cropontology.org/rdf/')
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
    g.bind('co', co)

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
        
        g.add((URIRef(p['orig_uri']), WUR_ont.has_biological_status, URIRef(p['mcpd_sampstat'])))  # temporary
        
        g.add((URIRef(p['orig_uri']), co['CO_020:0000011'], Literal(p['mcpd_accename'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000089'], Literal(p['mcpd_accenumb'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000024'], Literal(p['mcpd_donornumb'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000003'], Literal(p['mcpd_collnumb'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000025'], Literal(p['mcpd_othernumb'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000010'], Literal(p['mcpd_cropname'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000005'], Literal(p['mcpd_genus'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000006'], Literal(p['mcpd_species'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000007'], Literal(p['mcpd_spauthor'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000008'], Literal(p['mcpd_subtaxa'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000009'], Literal(p['mcpd_subtauthor'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000020'], Literal(p['mcpd_sampstat'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000107'], Literal(p['mcpd_mlsstat'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000078'], Literal(p['mcpd_storage'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000088'], Literal(p['mcpd_instcode'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000019'], Literal(p['mcpd_bredcode'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000097'], Literal(p['mcpd_bredname'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000004'], Literal(p['mcpd_collcode'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000111'], Literal(p['mcpd_collname'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000090'], Literal(p['mcpd_collinstaddress'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000091'], Literal(p['mcpd_collmissid'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000023'], Literal(p['mcpd_donorcode'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000104'], Literal(p['mcpd_donorname'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000026'], Literal(p['mcpd_duplsite'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000105'], Literal(p['mcpd_duplinstname'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000021'], Literal(p['mcpd_ancest'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000022'], Literal(p['mcpd_collsrc'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000095'], Literal(p['mcpd_coorddatum'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000094'], Literal(p['mcpd_coorduncert'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000013'], Literal(p['mcpd_origcty'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000014'], Literal(p['mcpd_collsite'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000017'], Literal(p['mcpd_elevation'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000096'], Literal(p['mcpd_georemeth'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000092'], Literal(p['mcpd_declatitude'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000015'], Literal(p['mcpd_latitude'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000093'], Literal(p['mcpd_declongitude'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000016'], Literal(p['mcpd_longitude'])))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000012'], Literal(p['mcpd_acqdate'], datatype=XSD.date)))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000018'], Literal(p['mcpd_colldate'], datatype=XSD.date)))
        g.add((URIRef(p['orig_uri']), co['CO_020:0000028'], Literal(p['mcpd_remarks'])))
        
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
    
    # remove triples with empty objects
    g.remove((None, None, Literal('')))
    g.remove((None, None, Literal('', datatype=XSD.date)))
    
    # print(experiments)
    # print(plants)
    # print(observations)
    
    # print(g.serialize(format='turtle'))
    g.serialize(destination='data2.ttl', format='turtle')
    print('Done.')


if __name__ == '__main__':
    path = 'data_template_v2.xlsx'
    template_to_triples(path)
