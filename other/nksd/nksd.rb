class Nksd
  def initialize(cipher='')
    @text=cipher
    @map={"2"=>"a","22"=>"b","222"=>"c",
      "3"=>"d","33"=>"e","333"=>"f",
      "4"=>"g","44"=>"h","444"=>"i",
      "5"=>"j","55"=>"k","555"=>"l",
      "6"=>"m","66"=>"n","666"=>"o",
      "7"=>"p","77"=>"q","777"=>"r","7777"=>"s",
      "8"=>"t","88"=>"u","888"=>"v",
      "9"=>"w","99"=>"x","999"=>"y","9999"=>"z","0"=>" "}
    #puts @map.inspect
  end
  def decode()
    msg=""
    key=""
    @text.each_char do |c|
      if key==""
        key=c
      elsif key[0].chr!=c
        msg<<lookUp(key)
        key=c
      else
        key<<c
      end
    end
    msg<<lookUp(key)
    msg
  end

  def lookUp(key="")
    if key== ""
      key
    elsif key==" "
      ""
    else
      @map[key]
    end
  end

end

if __FILE__==$0
  Nksd.new
end
