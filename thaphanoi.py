def thap_ha_noi(n,cot1,cot2,cot3):
    if n==1:
        print("chuyển đĩa",cot1,"sang",cot3)
    else:
        thap_ha_noi(n-1,cot1,cot3,cot2)
        print("chuyển đĩa",cot1,"sang",cot3)
        thap_ha_noi(n-1,cot2,cot1,cot3)

thap_ha_noi(3,"A","B","C")