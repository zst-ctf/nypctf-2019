#!/usr/bin/env ruby
require 'nokogiri'

# get picture order
array = {}

xml_str = File.read('word-document.xml').gsub(':', '')
doc = Nokogiri::XML(xml_str)
# puts doc
# puts doc.css('picpic')
for picture in doc.css('picpic') 
	pic_name = picture.css('piccNvPr')[0]['name']
	pic_id = picture.css('ablip')[0]['rembed']
	# puts pic_id + ', ' + pic_name

	array[pic_name] = pic_id
end

array = array.sort_by { |key, val| key.scan(/\d+/)[0].to_i }

array2 = {}
# get picture filename
xml_str = File.read('_rels-document.xml.rels').gsub(':', '')
doc = Nokogiri::XML(xml_str)
# puts doc
for rel in doc.css('Relationship') 
	rel_id = rel['Id']
	rel_target = rel['Target']
	# puts rel_id + ', ' + rel_target

	array2[rel_id] = rel_target
end

text = 'myo1u0xrknw'
flag = ''
array.each do |key, value|
	text_index = array2[value].scan(/\d+/)[0].to_i - 1
	puts key + ' = ' + value + ' = ' + array2[value] + ' = ' + text[text_index]
	flag += text[text_index]
end

puts flag
