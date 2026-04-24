module tb_dec_2_4;

logic E, B, C;
logic D0, D1, D2, D3;

decoder_2_4 Decoder_2_4(B, C, E, D0, D1, D2, D3);

initial 
begin
    $monitor($time, " E=%b, B=%b, C=%b, D0=%b, D1=%b, D2=%b, D3=%b, \n", 
                    E, B, C, D0, D1, D2, D3);    
    
    B = 0; C = 0; E = 0;
#5  B = 1;
#5  E = 1;
#5  C = 1;
#5  E = 0;
#5  $finish;
  
end
endmodule