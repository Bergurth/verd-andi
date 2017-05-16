"""
newOutput.py .. outside django
"""

from xml.dom import minidom

import sqlite3, csv

import sys
from os import path

from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree


conn = sqlite3.connect("../db.sqlite3")
c =conn.cursor()

"""
important tables

survey_item
survey_characteristic
survey_observation
survey_observedcharacteristic

item
..observation
...observedcharacteristic  ...  characteristic

"""

"""
<CrossSectionalData xmlns="http://www.SDMX.org/resources/SDMXML/schemas/v2_0/message" xmlns:cgs="urn:sdmx:org.sdmx.infomodel.keyfamily.KeyFamily=ESTAT:PPP_CGS:cross" xmlns:cross="http://www.SDMX.org/resources/SDMXML/schemas/v2_0/cross" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.SDMX.org/resources/SDMXML/schemas/v2_0/message SDMXMessage.xsd urn:sdmx:org.sdmx.infomodel.keyfamily.KeyFamily=ESTAT:PPP_CGS:cross ESTAT_PPP_CGS_COUNTRY_Cross.xsd http://www.SDMX.org/resources/SDMXML/schemas/v2_0/cross SDMXCrossSectionalData.xsd">
"""

root=Element('CrossSectionalData')
tree=ElementTree(root)
#xmlns=Element('xmlns')
# root.append(xmlns)
# xmlns.text("http://www.SDMX.org/resources/SDMXML/schemas/v2_0/message")

root.set('xmlns','http://www.SDMX.org/resources/SDMXML/schemas/v2_0/message')
root.set('xmlns:cgs',"urn:sdmx:org.sdmx.infomodel.keyfamily.KeyFamily=ESTAT:PPP_CGS:cross")
root.set('xmlns:cross',"http://www.SDMX.org/resources/SDMXML/schemas/v2_0/cross")
root.set('xmlns:xsi',"http://www.w3.org/2001/XMLSchema-instance")
root.set('xsi:schemaLocation',"http://www.SDMX.org/resources/SDMXML/schemas/v2_0/message SDMXMessage.xsd urn:sdmx:org.sdmx.infomodel.keyfamily.KeyFamily=ESTAT:PPP_CGS:cross ESTAT_PPP_CGS_COUNTRY_Cross.xsd http://www.SDMX.org/resources/SDMXML/schemas/v2_0/cross SDMXCrossSectionalData.xsd")

header = Element('Header')
root.append(header)
header_ID = Element('ID')


header.append(header_ID)
header_ID.text = 'PPP_SRVIC_3'

header_Test = Element('Test')
header_Test.text = 'false'
header.append(header_Test)

header_Truncated = Element('Truncated')
header_Truncated.text = 'false' 
header.append(header_Truncated)

header_Name = Element('Name')
header_Name.text = 'PPP Dataset'
header.append(header_Name)

header_Prepared = Element('Prepared') # date , timedate.now typathing  @dynam
header_Prepared.text = '2014-06-16T15:00:16+00:00'
header.append(header_Prepared)

header_Sender = Element('Sender')
header_Sender.set('id','IS')
header.append(header_Sender)

header_Sender_Name = Element('Name')
header_Sender_Name.text = 'Statistic Iceland'
header_Sender.append(header_Sender_Name)

header_Sender_Contact = Element('Contact')
header_Sender_Contact_Name = Element('Name')
header_Sender_Contact_Department = Element('Department')
header_Sender_Contact_Role = Element('Role')
header_Sender_Contact_Telephone = Element('Telephone')
header_Sender_Contact_Fax = Element('Fax')
header_Sender_Contact_Email = Element('Email')

header_Sender_Contact.append(header_Sender_Contact_Name)
header_Sender_Contact.append(header_Sender_Contact_Department)
header_Sender_Contact.append(header_Sender_Contact_Role)
header_Sender_Contact.append(header_Sender_Contact_Telephone)
header_Sender_Contact.append(header_Sender_Contact_Fax)
header_Sender_Contact.append(header_Sender_Contact_Email)

header_Sender.append(header_Sender_Contact)

header_Receiver = Element('Receiver')
header_Receiver.set('id','EUROSTAT')
header_Receiver_Name = Element('Name')
header_Receiver.append(header_Receiver_Name)

header.append(header_Receiver)

header_DataSetID = Element('DataSetID')
header_DataSetID.text = "PPP_SRVIC_3-2014-06-16T15:00:16"  # time stuff @dynam
header_DataSetAction = Element('DataSetAction')
header_DataSetAction.text = 'Append'
header_Extracted = Element('Extracted')
header_Extracted.text = '2014-06-16T15:00:16+00:00'
header_ReportingBegin = Element('ReportingBegin')
header_ReportingBegin.text = '2014-01-01'
header_ReportingEnd = Element('ReportingEnd')
header_ReportingEnd.text = '2014-12-31'

header.append(header_DataSetID)
header.append(header_DataSetAction)
header.append(header_Extracted)
header.append(header_ReportingBegin)
header.append(header_ReportingEnd)

# end header

cgs_dataset = Element('cgs:dataset')
cgs_group = Element('cgs:group')

cgs_dataset.append(cgs_group)


cgs_group.set('REFERENCE_YEAR','2014')   # @dynam year from survey
cgs_group.set('PPP_SURVEY','SRVIC')      # @dynam survey code
cgs_group.set('REPORTING_COUNTRY','IS')  
cgs_group.set('CURRENCY','ISK')

root.append(cgs_dataset)



c.execute('SELECT * FROM survey_item WHERE survey_id=1') # @dynam choose from current survey
item_rows = c.fetchall()


for i_row in item_rows:
	#print(i_row[0])
	# get commentary if exists.
	x_string = 'SELECT * FROM survey_itemcommentary WHERE item_id='+ '"' + i_row[0] + '"'
	c.execute(x_string)
	commentarys = c.fetchall()
	if (len(commentarys) > 0):
		commentary = commentarys[0]
		commentary_seasonality = "true" if commentary[0] else "false"
		commentary_representativity = "true" if commentary[4] else "false"
		commentary_comment = commentary[1]
		commentary_vat = str(commentary[2])
	else:
		commentary_vat = commentary_comment = commentary_representativity = commentary_seasonality = False
	
	# for loop later
	cgs_section = Element('cgs:Section')
	cgs_section.set("EPC_ITEM",i_row[0])
	cgs_section.set("VAT", commentary_vat if commentary_vat else "0.255")                   # almost static
	cgs_section.set("REPRESENTIVITY", commentary_representativity if commentary_representativity else "true")         # default to true  ---- later to be derived from new model ItemCommentary
	cgs_section.set("SEASONALITY", commentary_seasonality if commentary_seasonality else "false")          # default to false -----^
	cgs_section.set("ITEM_COMMENT", commentary_comment if commentary_comment else "")               # default to ""  ----------^
	cgs_section.set("FINALIZED","true")              # true

	cgs_group.append(cgs_section)
	# do a select query for observations and add to section, cgs_section.append()<-- observed price
	"""
	<cgs:OBSERVED_QUANTITY OBSERVATION_NUMBER="8" value="1.0" />
        <cgs:OBSERVED_PRICE OBSERVATION_NUMBER="9" OBS_TIME="2014-5" SHOP_TYPE="8" SHOP_IDENTIFIER="Skarinn Kringla" 
        OBS_COMMENT="" FLAG="O" DISCOUNT="N" value="2800.0" />
	"""
	item_i = i_row[0]
	#c.execute('SELECT * FROM survey_observation WHERE item_id={item_i}'.format(item_i=item_i))	
	# A.03.2.2.0.02.aa
	#c.execute('SELECT * FROM survey_observation WHERE item_id="A.09.4.1.0.01.ha"')
	execute_string = 'SELECT * FROM survey_observation WHERE item_id=' + '"' + item_i + '"'
	#print(execute_string)
	c.execute(execute_string)
	observations = c.fetchall()
	if(len(observations) > 0):
		observation_number = 1
		for obs_i in observations:
			# create observed_quantity and observed-price
			# (11, u'2017-04-24', 99, u'eMart', u'O', u'N', 15, u'Biggys', 30, u'flaggelation',
			# u'', u'A.09.4.1.0.01.ha', 1, 1, None)
			# (31, None, u'2017-04-27', 12, u'charlies', u'O', u'N', 60, 1, u'nice', u'', 
			# u'A.03.2.2.0.02.aa', 1, 1)
			cgs_observed_price = Element('cgs:OBSERVED_PRICE')
			cgs_observed_price.set('OBSERVATION_NUMBER',str(observation_number))
			cgs_observed_price.set('OBS_TIME', str(obs_i[2]))
			cgs_observed_price.set('SHOP_TYPE', str(obs_i[3]))
			cgs_observed_price.set('SHOP_IDENTIFIER', str(obs_i[4]))
			cgs_observed_price.set('OBS_COMMENT', str(obs_i[9]))
			cgs_observed_price.set('FLAG', str(obs_i[5]))
			cgs_observed_price.set('DISCOUNT', str(obs_i[6]))
			cgs_observed_price.set('value', str(obs_i[7]))

			cgs_section.append(cgs_observed_price)

			cgs_observed_quantity = Element('cgs:OBSERVED_QUANTITY')
			cgs_observed_quantity.set('OBSERVATION_NUMBER', str(observation_number))
			cgs_observed_quantity.set('value', str(obs_i[8]))

			cgs_section.append(cgs_observed_quantity)

			observation_number += 1
			# query for observed chars, create list and add | inbetween,... obs_i[0]
			execute_string2 = 'SELECT * FROM survey_observedcharacteristic WHERE observation_id=' + '"' + str(obs_i[0]) + '"'
			c.execute(execute_string2)
			observedcharacteristics = c.fetchall()

			# [(14, 2872, 17, u'perv')]    <------ example of one
			#  (id,id_of_char,id_of_obs ,value)
			char_arr = []
			for obs_char in observedcharacteristics:
				obs_char_id = obs_char[0]
				char_id = obs_char[1]
				obs_id = obs_char[2]
				obs_char_value = obs_char[3]
				execute_string3 = 'SELECT * FROM  survey_characteristic WHERE id=' + '"' + str(char_id) + '"'
				c.execute(execute_string3)
				characteristic_i = c.fetchall()
				char_name = characteristic_i[0][1]
				# get char Name 
				"""
				<cgs:OBSERVED_PRICE OBSERVATION_NUMBER="4" OBS_TIME="2014-5" 
				SHOP_TYPE="8" SHOP_IDENTIFIER="Rafholt" OBS_COMMENT="" FLAG="O" 
				DISCOUNT="N" value="25500.0" CHARACTERISTICS="Price of materials=8000|
				Travel costs=3500|Number of hours worked=2" CHARS_SEPARATOR="|" />
				"""
				# set observed price CHARACTERISTICS, CHARS_SEPARATOR='|'
				char_arr.append(str(char_name)+"="+str(obs_char_value))
				

			if (len(char_arr) > 0):
				char_string='|'.join(char_arr)
				cgs_observed_price.set("CHARACTERISTICS",char_string)
				cgs_observed_price.set("CHAR_SEPARATOR","|")

print etree.tostring(root)
#tree.write(open('person.xml','w'))



