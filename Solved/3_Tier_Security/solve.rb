require "wavefile"
include WaveFile

########################################################
## retrieve high and low bits
bool_buffer = []
threshold = 500

Reader.new("transmission.wav").each_buffer do |buffer|
	for s in buffer.samples
		is_high = (s.abs != 128) ? 1 : 0
		bool_buffer.push(is_high)
	end
end

#puts bool_buffer.join(',')

########################################################
## convert to (amplitude, length)

# split based on same chars, https://stackoverflow.com/a/39030231
split_bool_buffer = bool_buffer.join('').scan(/0+|1+/)
# then count sample length
signal_buffer = split_bool_buffer.map { |st| [st[0], st.length] }
signal_buffer2 = split_bool_buffer.map { |st| st[0].to_s + '/' + st.length.to_s }
puts signal_buffer2.join(',')

########################################################
# Clean up these observations:
# 1/1452 = LONG HIGH
# 1/492 = SHORT HIGH
# 0/464 = gap between dits, dahs
# 0/1424 = gap between characters

morse_code_array = []

morse_code = ''
ditdah_count = 0
ditdah_count_2 = 0
ditdah_threshold = 45 

for sig in signal_buffer
	bit_type = sig[0]
	bit_length = sig[1]
	# puts(bit_type.to_s + '/' + bit_length.to_s)

	if bit_type == '1' then
		ditdah_count += 1
		if bit_length > 1000 then
			morse_code += '-'
		elsif bit_length > 400 then
			morse_code += '.'
		end
	else
		if bit_length > 1000 then
			morse_code_array.push(morse_code)
			morse_code = ''
		end
	end
end
# puts morse_code_array

########################################################
# Decode:
$morse_dict = {
    "a" => ".-","b" => "-...","c" => "-.-.","d" => "-..","e" => ".","f" => "..-.","g" => "--.","h" => "....","i" => "..","j" => ".---","k" => "-.-","l" => ".-..","m" => "--","n" => "-.","o" => "---","p" => ".--.","q" => "--.-","r" => ".-.","s" => "...","t" => "-","u" => "..-","v" => "...-","w" => ".--","x" => "-..-","y" => "-.--","z" => "--.."," " => " ","1" => ".----","2" => "..---","3" => "...--","4" => "....-","5" => ".....","6" => "-....","7" => "--...","8" => "---..","9" => "----.","0" => "-----"
}
def decode_morse(morse_code)
	# return $morse_dict.select{|key, val| val == morse_code }.keys
	return $morse_dict.key(morse_code) || '?'
end


decoded_array = morse_code_array.map { |code| decode_morse(code) }

puts morse_code_array.join(' ')
puts decoded_array.join('')
