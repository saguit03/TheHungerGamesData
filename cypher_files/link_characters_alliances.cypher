MATCH (c:Character {ID: '0'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '1'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '2'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '3'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '6'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '8'}), (k:Character {Name: 'Katniss Everdeen'})
CREATE (c)-[:ALLY_OF]->(k);
MATCH (c:Character {ID: '8'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '10'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '11'}), (a:Alliance {Name: 'Peacekeepers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '11'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '13'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '14'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '16'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '17'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '18'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '19'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '20'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '23'}), (k:Character {Name: 'Katniss Everdeen'})
CREATE (c)-[:ALLY_OF]->(k);
MATCH (c:Character {ID: '26'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '27'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '29'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '30'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '31'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '34'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '36'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '37'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '39'}), (a:Alliance {Name: 'Peacekeepers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '40'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '42'}), (k:Character {Name: 'Katniss Everdeen'})
CREATE (c)-[:ALLY_OF]->(k);
MATCH (c:Character {ID: '44'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '46'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '48'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '52'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '53'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '54'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '56'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '57'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '60'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '62'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '67'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '69'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '72'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '73'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '74'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '75'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '76'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '77'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '79'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '80'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '81'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '82'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '83'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '84'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '85'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '87'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '88'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '89'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '90'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '91'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '92'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '93'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '94'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '95'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '96'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '97'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '98'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '99'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '101'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '103'}), (a:Alliance {Name: 'Academy'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '104'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '104'}), (h:Character {Name: 'Haymitch Abernathy'})
CREATE (c)-[:ALLY_OF]->(h);
MATCH (c:Character {ID: '105'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '106'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '108'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '109'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '110'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '112'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '113'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '114'}), (k:Character {Name: 'Katniss Everdeen'})
CREATE (c)-[:ALLY_OF]->(k);
MATCH (c:Character {ID: '116'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '118'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '118'}), (k:Character {Name: 'Katniss Everdeen'})
CREATE (c)-[:ALLY_OF]->(k);
MATCH (c:Character {ID: '119'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '120'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '121'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '122'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '123'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '125'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '126'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '128'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '131'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '134'}), (a:Alliance {Name: 'Careers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '136'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '137'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '140'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '142'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '145'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '146'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '147'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '148'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '149'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '150'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '153'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '155'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '157'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '161'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '163'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '164'}), (a:Alliance {Name: 'Peacekeepers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '165'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '166'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '167'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '169'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '171'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '173'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '175'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '178'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '180'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '182'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '183'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '185'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '186'}), (a:Alliance {Name: 'Peacekeepers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '187'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '188'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '190'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '191'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '194'}), (k:Character {Name: 'Katniss Everdeen'})
CREATE (c)-[:ALLY_OF]->(k);
MATCH (c:Character {ID: '195'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '197'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '198'}), (a:Alliance {Name: 'Peacekeepers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '200'}), (k:Character {Name: 'Katniss Everdeen'})
CREATE (c)-[:ALLY_OF]->(k);
MATCH (c:Character {ID: '201'}), (k:Character {Name: 'Katniss Everdeen'})
CREATE (c)-[:ALLY_OF]->(k);
MATCH (c:Character {ID: '202'}), (a:Alliance {Name: 'Covey'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '204'}), (a:Alliance {Name: 'Covey'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '206'}), (h:Character {Name: 'Haymitch Abernathy'})
CREATE (c)-[:ALLY_OF]->(h);
MATCH (c:Character {ID: '207'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '208'}), (a:Alliance {Name: 'Covey'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '210'}), (k:Character {Name: 'Katniss Everdeen'})
CREATE (c)-[:ALLY_OF]->(k);
MATCH (c:Character {ID: '213'}), (a:Alliance {Name: 'Covey'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '214'}), (a:Alliance {Name: 'Peacekeepers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '215'}), (a:Alliance {Name: 'Peacekeepers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '216'}), (a:Alliance {Name: 'Peacekeepers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '217'}), (a:Alliance {Name: 'Peacekeepers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '219'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '220'}), (k:Character {Name: 'Katniss Everdeen'})
CREATE (c)-[:ALLY_OF]->(k);
MATCH (c:Character {ID: '221'}), (h:Character {Name: 'Haymitch Abernathy'})
CREATE (c)-[:ALLY_OF]->(h);
MATCH (c:Character {ID: '222'}), (h:Character {Name: 'Haymitch Abernathy'})
CREATE (c)-[:ALLY_OF]->(h);
MATCH (c:Character {ID: '227'}), (k:Character {Name: 'Katniss Everdeen'})
CREATE (c)-[:ALLY_OF]->(k);
MATCH (c:Character {ID: '228'}), (k:Character {Name: 'Katniss Everdeen'})
CREATE (c)-[:ALLY_OF]->(k);
MATCH (c:Character {ID: '230'}), (a:Alliance {Name: 'Covey'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '231'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '232'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '233'}), (a:Alliance {Name: 'Covey'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '236'}), (a:Alliance {Name: 'Covey'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '241'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '245'}), (k:Character {Name: 'Katniss Everdeen'})
CREATE (c)-[:ALLY_OF]->(k);
MATCH (c:Character {ID: '248'}), (a:Alliance {Name: 'Peacekeepers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '250'}), (a:Alliance {Name: 'Peacekeepers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '254'}), (a:Alliance {Name: 'Covey'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '256'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '257'}), (a:Alliance {Name: 'Covey'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '260'}), (h:Character {Name: 'Haymitch Abernathy'})
CREATE (c)-[:ALLY_OF]->(h);
MATCH (c:Character {ID: '262'}), (a:Alliance {Name: 'Newcomers'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '263'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '264'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '265'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '266'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '267'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '268'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '269'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '270'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '271'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
MATCH (c:Character {ID: '272'}), (a:Alliance {Name: 'Rebels'})
CREATE (c)-[:BELONGS_TO]->(a);
