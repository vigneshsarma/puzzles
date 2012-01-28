require 'prime'

describe Prime do

  it "convert the given string to equvalent integer" do
    prime=Prime.new "10"
    #prime.limit.should eq(10)
    prime.sum.should eq(17)
    prime1=Prime.new "20"
    #prime1.limit.should eq(20)
  end
  it "isPrime should check whether the given int is prime or not" do
    prime=Prime.new "10"    
    prime.is_prime?(5).should eq(true)
    prime.is_prime?(2).should eq(true)
    prime.is_prime?(3).should eq(true)
    prime.is_prime?(4).should eq(false)
    prime.is_prime?(9).should eq(false)
    #prime.is_prime?(1).should eq(false)
    #prime.is_prime?(0).should eq(false)
    prime.isPrime?(5).should eq(true)
    prime.isPrime?(2).should eq(true)
    prime.isPrime?(3).should eq(true)
    prime.isPrime?(4).should eq(false)
    prime.isPrime?(9).should eq(false)
    prime.isPrime?(1).should eq(false)
    prime.isPrime?(0).should eq(false)
  end

  
  
end
