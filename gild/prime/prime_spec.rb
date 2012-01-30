require 'prime'

describe Prime do

  it "convert the given string to equvalent integer" do
    prime=Prime.new "10"
    #prime.limit.should eq(10)
    prime.sum.should eq(17)
    prime1=Prime.new "534"
    #prime1.limit.should eq(20)
    #prime1.sum.should eq(23592)
    #prime1=Prime.new "2497236"
  end
  
  it "isPrime should check whether the given int is prime or not" do
    prime=Prime.new "10"    

    prime.prime?(5).should eq(true)
    prime.prime?(2).should eq(true)
    prime.prime?(3).should eq(true)
    prime.prime?(4).should eq(false)
    prime.prime?(9).should eq(false)
    prime.prime?(1).should eq(false)
    prime.prime?(0).should eq(false)
  end

  
  
end
