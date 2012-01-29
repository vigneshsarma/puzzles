#!/usr/bin/ruby

class Sopa
  def initialize(cipher=0,text='')
    @key=(cipher.to_i)%26
    @text=text
    @relate=Hash.new()
  end
  def mapCipher(from,to)
    a=from[0]
    z=to[0]
    (a..z).each do |elm|
      if (elm-@key) <a
        @relate[elm.chr]=((z+1-(a-(elm-@key))).chr)
      else
        @relate[elm.chr]=((elm - @key).chr)
      end
    end
  end
  def decript()
    detext=""
    mapCipher("a","z")
    mapCipher("A","Z")
    #print @relate.inspect
    #print @key
    
    @text.each_char do |alpha|
      if @relate.has_key?(alpha)
        print @relate[alpha]
        #print "this "
      else
        print alpha
      end
    end
    #puts detext
  end
end

if __FILE__ == $0
  text=""
  file=File.new(ARGV[0],"r")
  key=file.gets
  #print line[0..-2]
  while line=file.gets do
    text<<line
  end
  #print line
  sopa=Sopa.new(key[0..-2],text)
  sopa.decript
end
