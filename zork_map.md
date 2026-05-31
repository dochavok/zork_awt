# Zork I — Room Connection Map

**Legend**
- `---` open bidirectional passage
- `-.->` conditional or one-way passage
- `-->` strictly one-way
- Edge labels describe the condition or notable direction
- *diode* = maze one-way warning passage (no return)

```mermaid
graph TD

  subgraph SFC["Surface"]
    WOH[West of House]
    NOH[North of House]
    SOH[South of House]
    EOH[Behind House]
    SBAR[Stone Barrow]
    F1[Forest]
    F2[Forest]
    F3[Forest]
    MTN[Mountains]
    FP[Forest Path]
    UAT[Up a Tree]
    GC[Grating Clearing]
    CLR[Clearing]
    CYV[Canyon View]
    CYM[Rocky Ledge]
    CYB[Canyon Bottom]
    EOR[End of Rainbow]
    ONR[On the Rainbow]
    ARF[Aragain Falls]
    SHR[Shore]
    SBH[Sandy Beach]
    SCAV[Sandy Cave]
  end

  subgraph HSE["House"]
    KIT[Kitchen]
    ATT[Attic]
    LR[Living Room]
  end

  subgraph L1["Underground L1"]
    CEL[Cellar]
    TRL[Troll Room]
    EOC[East of Chasm]
    GAL[Gallery]
    STD[Studio]
    EWP[E-W Passage]
    RND[Round Room]
    NSP[N-S Passage]
    CHS[Chasm]
    ENG[Engravings Cave]
    DOM[Dome Room]
    TOR[Torch Room]
    NTP[Temple]
    ALT[Altar]
    EGY[Egyptian Room]
    DPC[Deep Canyon]
    LUD[Loud Room]
    DMP[Damp Cave]
  end

  subgraph MZE["Maze"]
    M1[Maze 1]
    M2[Maze 2]
    M3[Maze 3]
    M4[Maze 4]
    M5[Maze 5]
    M6[Maze 6]
    M7[Maze 7]
    M8[Maze 8]
    M9[Maze 9]
    M10[Maze 10]
    M11[Maze 11]
    M12[Maze 12]
    M13[Maze 13]
    M14[Maze 14]
    M15[Maze 15]
    DE1[Dead End]
    DE2[Dead End]
    DE3[Dead End]
    DE4[Dead End]
    GRM[Grating Room]
    CYC[Cyclops Room]
    TRS[Treasure Room]
    STP[Strange Passage]
  end

  subgraph DEP["Deep Underground"]
    RS[Reservoir South]
    RES[Reservoir]
    RN[Reservoir North]
    STV[Stream View]
    IST[In Stream]
    ATL[Atlantis Room]
    MR1[Mirror Room]
    MR2[Mirror Room]
    SMCV[Small Cave]
    TCV[Tiny Cave]
    CLD[Cold Passage]
    NRP[Narrow Passage]
    WNP[Winding Passage]
    TWP[Twisting Passage]
    SLR[Slide Room]
  end

  subgraph DAMA["Dam and River"]
    DAM[Dam]
    DLB[Dam Lobby]
    MNT[Maintenance Room]
    DBZ[Dam Base]
    WCN[White Cliffs Beach N]
    WCS[White Cliffs Beach S]
    R1[Frigid River 1]
    R2[Frigid River 2]
    R3[Frigid River 3]
    R4[Frigid River 4]
    R5[Frigid River 5]
  end

  subgraph HAD["Hades"]
    ETH[Entrance to Hades]
    LLD[Land of the Dead]
  end

  subgraph MINE["Coal Mine"]
    MNE[Mine Entrance]
    SQR[Squeaky Room]
    BAT[Bat Room]
    SFR[Shaft Room]
    SMR[Smelly Room]
    GSR[Gas Room]
    MI1[Coal Mine 1]
    MI2[Coal Mine 2]
    MI3[Coal Mine 3]
    MI4[Coal Mine 4]
    LDT[Ladder Top]
    LDB[Ladder Bottom]
    DE5[Dead End]
    TBR[Timber Room]
    LSH[Drafty Room]
    MCR[Machine Room]
  end

  %% ═══ Surface ═════════════════════════════════════════════════
  WOH --- NOH
  WOH --- SOH
  WOH --- F1
  WOH -.->|won-flag| SBAR
  SBAR --> WOH
  NOH --- EOH
  SOH --- EOH
  SOH --- F3
  F1 --- FP
  F1 --- GC
  F1 --- F3
  F2 --- MTN
  F2 --- FP
  F2 --- CLR
  F3 --- CLR
  FP --- GC
  FP --- UAT
  CLR --- CYV
  CYV --- CYM
  CYM --- CYB
  CYB --- EOR
  EOR -.->|rainbow-flag| ONR
  ONR --- ARF
  ARF --- SHR
  SHR --- SBH
  SBH --- SCAV

  %% ═══ House ═══════════════════════════════════════════════════
  KIT --- ATT
  KIT --- LR
  EOH -.->|window open| KIT
  LR -.->|trapdoor| CEL
  LR -.->|magic-flag| STP
  KIT -.->|chimney up| STD

  %% ═══ Underground L1 ══════════════════════════════════════════
  CEL --- TRL
  CEL --- EOC
  EOC --- GAL
  GAL --- STD
  TRL -.->|troll gone| EWP
  TRL -.->|troll gone| M1
  EWP --- RND
  EWP --- CHS
  RND --- LUD
  RND --- NSP
  RND --- ENG
  RND --- NRP
  NSP --- CHS
  NSP --- DPC
  CHS --- RS
  DPC --- RS
  DPC --- DAM
  DPC --- LUD
  ENG --- DOM
  DOM -.->|rope| TOR
  TOR --- NTP
  NTP --- ALT
  NTP --- EGY
  LUD --- DMP
  DMP --- WCN
  ALT -.->|coffin-cure| TCV

  %% ═══ Surface ↔ Maze (Grating) ════════════════════════════════
  GC -.->|grate open| GRM
  GRM -.->|grate open| GC

  %% ═══ Maze ════════════════════════════════════════════════════
  M1 --- M2
  M1 --- M4
  M2 --- M3
  M2 -.->|diode| M4
  M3 --- M4
  M3 -.->|diode| M5
  M4 --- DE1
  M5 --- DE2
  M5 --- M6
  M6 --- M7
  M6 --- M9
  M7 --- M8
  M7 --- M14
  M7 --- M15
  M7 -.->|diode| DE1
  M8 --- DE3
  M9 --- M10
  M9 --- M12
  M9 --- M13
  M9 -.->|diode| M11
  M10 --- M11
  M10 --- M13
  M11 --- GRM
  M11 --- M13
  M12 -.->|diode| M5
  M12 --- M11
  M12 --- M13
  M12 --- DE4
  M14 --- M15
  M15 --- CYC
  CYC -.->|magic-flag| STP
  CYC -.->|cyclops gone| TRS
  STP --- LR

  %% ═══ Deep Underground ════════════════════════════════════════
  RS --- STV
  RS -.->|low-tide| RES
  RES --- RN
  RES --- IST
  STV --- IST
  RN --- ATL
  ATL --- SMCV
  SMCV --- MR1
  SMCV --- TWP
  MR1 --- CLD
  MR1 --- TWP
  MR2 --- NRP
  MR2 --- WNP
  TCV --- MR2
  TCV --- WNP
  TCV --> ETH
  CLD --- SLR
  TWP --- SMCV
  WNP --- TCV
  SLR --- MNE
  SLR --> CEL

  %% ═══ Dam and River ═══════════════════════════════════════════
  DAM --- DLB
  DAM --- DBZ
  DLB --- MNT
  DBZ --- R1
  R1 --- R2
  R2 --- R3
  R3 --- R4
  R4 --- R5
  R3 --- WCN
  R4 --- WCS
  R4 --- SBH
  R5 --- SHR
  WCN -.->|deflate| WCS
  WCS -.->|deflate| WCN

  %% ═══ Hades ═══════════════════════════════════════════════════
  ETH -.->|LLD-flag| LLD
  LLD --> ETH

  %% ═══ Coal Mine ═══════════════════════════════════════════════
  MNE --- SQR
  SQR --- BAT
  BAT --- SFR
  SFR --- SMR
  SMR --- GSR
  GSR --- MI1
  MI1 --- MI2
  MI2 --- MI3
  MI3 --- MI4
  MI4 --- LDT
  LDT --- LDB
  LDB --- DE5
  LDB --- TBR
  TBR -.->|empty-handed| LSH
  LSH --- MCR
```
