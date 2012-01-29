#!/usr/bin/ruby
class Sopa
  def initialize(cipher=0,text='')
    @cipher=cipher.to_i
    @text=text
  end
  def decript()
    key=@cipher%26
    detext=""
    @text.each_byte do |alpha|
      #print alpha
      if (alpha >= ?a and alpha <= ?z)
        if (alpha-key) <?a
          detext<<((?z+1-(?a-(alpha-key))).chr)
        else
          detext<<((alpha - key).chr)
        end
      elsif (alpha >=?A and alpha <=?Z)
        detext<<if (alpha-key) <?A
                  ((?Z+1-(?A-(alpha-key))).chr)
        else
          ((alpha - key).chr)
        end
      else
       detext<<alpha.chr
      end
    end
    #f=File.open(ARGV[0][0..-4]+".out","w")
    #f.write(detext)
    puts detext
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
