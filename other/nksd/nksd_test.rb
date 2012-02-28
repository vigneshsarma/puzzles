require 'nksd'

describe Nksd do
  it "decoder the real message from" do
    cipher="6885558 8866887777"
    cipher1="2 22"
    nksd = Nksd.new cipher
    nksd.decode.should eq("multunus")
    nksd = Nksd.new cipher1
    nksd.decode.should eq("ab")
  end

  it "decoder the real message from" do
    nksd = Nksd.new "" 
    nksd.lookUp("2").should eq("a")
    nksd.lookUp("2222").should eq("a")
    nksd.lookUp("999999").should eq("x")
  end

end
