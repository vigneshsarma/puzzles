#!/usr/bin/ruby

class Tower
  attr_accessor :particp
  def initialize(text='')
    @map={}
    @particp=[]
    digit=""
    individ=Array.new
    text.each_char do |alpha|
      if alpha==="("
        digit=""
        individ=Array.new
      elsif alpha===" "
        #print "next person"
      elsif alpha===","
        individ.push(digit.to_i)
        digit=""
      elsif alpha===")"
        individ.push(digit.to_i)
        @particp.push(individ)
      else
        digit<<alpha
      end
    end
    @sortedByFirst=@particp.sort {|one , two| one[0]<=>two[0]}
    process @sortedByFirst
  end
  
  def process(sortedList)
    maxHight=0
    (0..(sortedList.length-1)).each do |elm|
      if not @map.has_key?(sortedList[elm])
        findMaxHight(sortedList[(elm+1)..-1],sortedList[elm])
      end
      if @map[sortedList[elm]]>maxHight
        maxHight=@map[sortedList[elm]]
      end
    end
    puts maxHight
  end
  
  def findMaxHight(sortedList,cmp)
    maxVal=1
    (0..(sortedList.length-1)).each do |elm|
      if sortedList[elm][1]>cmp[1]
        val=if @map.has_key?(sortedList[elm])
              @map[(sortedList[elm])]+1
            else
              (findMaxHight(sortedList[(elm+1)..-1],sortedList[elm])+1)
            end
        if val> maxVal
          maxVal=val
        end
      end
    end
    @map[cmp]=maxVal
  end  
  
end

if __FILE__ == $0
  text=""
  file=File.new(ARGV[0],"r")
  key=file.gets
  tower=Tower.new(key[0..-2])
end
