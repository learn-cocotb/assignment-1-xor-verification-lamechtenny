module exor_test(
                input wire a,b,
                output wire y);
  //module call
  exor uut(.a(a),.b(b),.y(y));
  
  initial 
    begin
      $dumpfile("waves.vcd");
      $dumpvars;
    end
  
endmodule
