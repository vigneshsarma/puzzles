#!/usr/bin/ruby

class Prime
  attr_accessor :limit ,:sum
  def initialize(limit='')
    @limit=limit.to_i
    @sum=0
    (2..@limit).each do |num|
      if is_prime?(num)
        @sum+=num
      end
    end
    puts @sum
  end
  def is_prime?(n)
    return true if n == 2
    return false if n & 1 == 0 
    # runs the block for each number from 2 to sqrt(n)
    # only returns true if the block *never* returns true
    (3..(Math.sqrt(n).to_i)).step(2).none? { |i| n%i == 0 }
  end

  def isPrime?(number)
    limit=Math.sqrt(number)
    if number===1 or number === 0 or limit=== Integer(limit)
      return false
    end
    (2..limit).each do |check|
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
