#!/usr/bin/ruby

class Prime
  attr_accessor :limit ,:sum
  def initialize(limit='')
    @limit=limit.to_i
    @sum=0
    @allPrimes=[]
    (2..@limit).each do |num|
      if prime?(num)
        @sum+=num
        @allPrimes.push num
        puts num
      end
    end
    puts @sum
  end

  def prime?(number)
    limit=Math.sqrt(number)
    if number===1 or number === 0 or limit=== Integer(limit)
      return false
    end
    @allPrimes.each do |check|
      return true if check >limit
      if number%check===0
        return false
      end
    end
    true
  end
end

if __FILE__ == $0
  text=""
  file=File.new(ARGV[0],"r")
  key=file.gets
  prime=Prime.new(key.sub("\n",""))
end
