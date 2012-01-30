require 'tower'

describe Tower do

  it "should decode the text into an array" do
    @tower=Tower.new "(15, 176) (65, 97) (72, 43) (102, 6) (191, 189) (90, 163) (44, 168) (39, 47) (123, 37)"
    @tower.particp.should eq([[15, 176], [65, 97], [72, 43], [102, 6], [191, 189], [90, 163], [44, 168], [39, 47], [123, 37]])
  end
  
  
  
end
