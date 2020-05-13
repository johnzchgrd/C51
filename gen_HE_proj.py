### config ####
import os
SE_no = 1
num_subclass = [2, 1, 2]
filetype = "c"

#########
typelist = {
    "asm": 2,
    "c": 1
}
typetemplates = {
    "asm": "",  # writes nothing
    "c": '''#include <reg51.h>

void main()
{
    // init

    // loop
    while(1)
    {
        // do something.
    }
}

'''
}

# file content
multi_s0 = '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
<ProjectWorkspace xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="project_mpw.xsd">

  <SchemaVersion>1.0</SchemaVersion>

  <Header>### uVision Project, (C) Keil Software</Header>

  <WorkspaceName>WorkSpace</WorkspaceName>
'''
# maybe add active ?
multi_t_dd = '''

  <project>
    <PathAndName>.\\sub_prjs\\HE%d_%d.uvproj</PathAndName>
    <NodeIsExpanded>1</NodeIsExpanded>
  </project>
'''
multi_e0 = '''
</ProjectWorkspace>
'''
uvproj_s_dd_dds_d_dds = '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
<Project xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="project_proj.xsd">

  <SchemaVersion>1.1</SchemaVersion>

  <Header>### uVision Project, (C) Keil Software</Header>

  <Targets>
    <Target>
      <TargetName>he%d_%d</TargetName>
      <ToolsetNumber>0x0</ToolsetNumber>
      <ToolsetName>MCS-51</ToolsetName>
      <uAC6>0</uAC6>
      <TargetOption>
        <TargetCommonOption>
          <Device>AT89C51</Device>
          <Vendor>Atmel</Vendor>
          <Cpu>IRAM(0-0xFF) IROM(0-0x1FFF) CLOCK(24000000)</Cpu>
          <FlashUtilSpec></FlashUtilSpec>
          <StartupFile>"LIB\\STARTUP.A51" ("Standard 8051 Startup Code")</StartupFile>
          <FlashDriverDll></FlashDriverDll>
          <DeviceId>2976</DeviceId>
          <RegisterFile>REGX51.H</RegisterFile>
          <MemoryEnv></MemoryEnv>
          <Cmp></Cmp>
          <Asm></Asm>
          <Linker></Linker>
          <OHString></OHString>
          <InfinionOptionDll></InfinionOptionDll>
          <SLE66CMisc></SLE66CMisc>
          <SLE66AMisc></SLE66AMisc>
          <SLE66LinkerMisc></SLE66LinkerMisc>
          <SFDFile></SFDFile>
          <bCustSvd>0</bCustSvd>
          <UseEnv>0</UseEnv>
          <BinPath>C:\\Keil_v5\\C51\\BIN\\</BinPath>
          <IncludePath></IncludePath>
          <LibPath></LibPath>
          <RegisterFilePath></RegisterFilePath>
          <DBRegisterFilePath>Atmel\\</DBRegisterFilePath>
          <TargetStatus>
            <Error>0</Error>
            <ExitCodeStop>0</ExitCodeStop>
            <ButtonStop>0</ButtonStop>
            <NotGenerated>0</NotGenerated>
            <InvalidFlash>1</InvalidFlash>
          </TargetStatus>
          <OutputDirectory>.\\obj\\</OutputDirectory>
          <OutputName>SE1</OutputName>
          <CreateExecutable>1</CreateExecutable>
          <CreateLib>0</CreateLib>
          <CreateHexFile>1</CreateHexFile>
          <DebugInformation>1</DebugInformation>
          <BrowseInformation>1</BrowseInformation>
          <ListingPath>.\\lst\\</ListingPath>
          <HexFormatSelection>0</HexFormatSelection>
          <Merge32K>0</Merge32K>
          <CreateBatchFile>0</CreateBatchFile>
          <BeforeCompile>
            <RunUserProg1>0</RunUserProg1>
            <RunUserProg2>0</RunUserProg2>
            <UserProg1Name></UserProg1Name>
            <UserProg2Name></UserProg2Name>
            <UserProg1Dos16Mode>0</UserProg1Dos16Mode>
            <UserProg2Dos16Mode>0</UserProg2Dos16Mode>
            <nStopU1X>0</nStopU1X>
            <nStopU2X>0</nStopU2X>
          </BeforeCompile>
          <BeforeMake>
            <RunUserProg1>0</RunUserProg1>
            <RunUserProg2>0</RunUserProg2>
            <UserProg1Name></UserProg1Name>
            <UserProg2Name></UserProg2Name>
            <UserProg1Dos16Mode>0</UserProg1Dos16Mode>
            <UserProg2Dos16Mode>0</UserProg2Dos16Mode>
            <nStopB1X>0</nStopB1X>
            <nStopB2X>0</nStopB2X>
          </BeforeMake>
          <AfterMake>
            <RunUserProg1>0</RunUserProg1>
            <RunUserProg2>0</RunUserProg2>
            <UserProg1Name></UserProg1Name>
            <UserProg2Name></UserProg2Name>
            <UserProg1Dos16Mode>0</UserProg1Dos16Mode>
            <UserProg2Dos16Mode>0</UserProg2Dos16Mode>
            <nStopA1X>0</nStopA1X>
            <nStopA2X>0</nStopA2X>
          </AfterMake>
          <SelectedForBatchBuild>0</SelectedForBatchBuild>
          <SVCSIdString></SVCSIdString>
        </TargetCommonOption>
        <CommonProperty>
          <UseCPPCompiler>0</UseCPPCompiler>
          <RVCTCodeConst>0</RVCTCodeConst>
          <RVCTZI>0</RVCTZI>
          <RVCTOtherData>0</RVCTOtherData>
          <ModuleSelection>0</ModuleSelection>
          <IncludeInBuild>1</IncludeInBuild>
          <AlwaysBuild>0</AlwaysBuild>
          <GenerateAssemblyFile>0</GenerateAssemblyFile>
          <AssembleAssemblyFile>0</AssembleAssemblyFile>
          <PublicsOnly>0</PublicsOnly>
          <StopOnExitCode>3</StopOnExitCode>
          <CustomArgument></CustomArgument>
          <IncludeLibraryModules></IncludeLibraryModules>
          <ComprImg>1</ComprImg>
          <BankNo>65535</BankNo>
        </CommonProperty>
        <DllOption>
          <SimDllName>S8051.DLL</SimDllName>
          <SimDllArguments></SimDllArguments>
          <SimDlgDll>DP51.DLL</SimDlgDll>
          <SimDlgDllArguments>-p52</SimDlgDllArguments>
          <TargetDllName>S8051.DLL</TargetDllName>
          <TargetDllArguments></TargetDllArguments>
          <TargetDlgDll>TP51.DLL</TargetDlgDll>
          <TargetDlgDllArguments>-p52</TargetDlgDllArguments>
        </DllOption>
        <DebugOption>
          <OPTHX>
            <HexSelection>0</HexSelection>
            <HexRangeLowAddress>0</HexRangeLowAddress>
            <HexRangeHighAddress>0</HexRangeHighAddress>
            <HexOffset>0</HexOffset>
            <Oh166RecLen>16</Oh166RecLen>
          </OPTHX>
          <Simulator>
            <UseSimulator>1</UseSimulator>
            <LoadApplicationAtStartup>1</LoadApplicationAtStartup>
            <RunToMain>1</RunToMain>
            <RestoreBreakpoints>1</RestoreBreakpoints>
            <RestoreWatchpoints>1</RestoreWatchpoints>
            <RestoreMemoryDisplay>1</RestoreMemoryDisplay>
            <RestoreFunctions>1</RestoreFunctions>
            <RestoreToolbox>1</RestoreToolbox>
            <LimitSpeedToRealTime>0</LimitSpeedToRealTime>
            <RestoreSysVw>1</RestoreSysVw>
          </Simulator>
          <Target>
            <UseTarget>0</UseTarget>
            <LoadApplicationAtStartup>1</LoadApplicationAtStartup>
            <RunToMain>0</RunToMain>
            <RestoreBreakpoints>1</RestoreBreakpoints>
            <RestoreWatchpoints>1</RestoreWatchpoints>
            <RestoreMemoryDisplay>1</RestoreMemoryDisplay>
            <RestoreFunctions>0</RestoreFunctions>
            <RestoreToolbox>1</RestoreToolbox>
            <RestoreTracepoints>0</RestoreTracepoints>
            <RestoreSysVw>1</RestoreSysVw>
          </Target>
          <RunDebugAfterBuild>0</RunDebugAfterBuild>
          <TargetSelection>-1</TargetSelection>
          <SimDlls>
            <CpuDll></CpuDll>
            <CpuDllArguments></CpuDllArguments>
            <PeripheralDll></PeripheralDll>
            <PeripheralDllArguments></PeripheralDllArguments>
            <InitializationFile></InitializationFile>
          </SimDlls>
          <TargetDlls>
            <CpuDll></CpuDll>
            <CpuDllArguments></CpuDllArguments>
            <PeripheralDll></PeripheralDll>
            <PeripheralDllArguments></PeripheralDllArguments>
            <InitializationFile></InitializationFile>
            <Driver></Driver>
          </TargetDlls>
        </DebugOption>
        <Utilities>
          <Flash1>
            <UseTargetDll>0</UseTargetDll>
            <UseExternalTool>0</UseExternalTool>
            <RunIndependent>0</RunIndependent>
            <UpdateFlashBeforeDebugging>0</UpdateFlashBeforeDebugging>
            <Capability>0</Capability>
            <DriverSelection>-1</DriverSelection>
          </Flash1>
          <bUseTDR>0</bUseTDR>
          <Flash2></Flash2>
          <Flash3></Flash3>
          <Flash4></Flash4>
          <pFcarmOut></pFcarmOut>
          <pFcarmGrp></pFcarmGrp>
          <pFcArmRoot></pFcArmRoot>
          <FcArmLst>0</FcArmLst>
        </Utilities>
        <Target51>
          <Target51Misc>
            <MemoryModel>0</MemoryModel>
            <RTOS>0</RTOS>
            <RomSize>2</RomSize>
            <DataHold>0</DataHold>
            <XDataHold>0</XDataHold>
            <UseOnchipRom>0</UseOnchipRom>
            <UseOnchipArithmetic>0</UseOnchipArithmetic>
            <UseMultipleDPTR>0</UseMultipleDPTR>
            <UseOnchipXram>0</UseOnchipXram>
            <HadIRAM>1</HadIRAM>
            <HadXRAM>0</HadXRAM>
            <HadIROM>1</HadIROM>
            <Moda2>0</Moda2>
            <Moddp2>0</Moddp2>
            <Modp2>0</Modp2>
            <Mod517dp>0</Mod517dp>
            <Mod517au>0</Mod517au>
            <Mode2>0</Mode2>
            <useCB>0</useCB>
            <useXB>0</useXB>
            <useL251>0</useL251>
            <useA251>0</useA251>
            <Mx51>0</Mx51>
            <ModC812>0</ModC812>
            <ModCont>0</ModCont>
            <Lp51>0</Lp51>
            <useXBS>0</useXBS>
            <ModDA>0</ModDA>
            <ModAB2>0</ModAB2>
            <Mx51P>0</Mx51P>
            <hadXRAM2>0</hadXRAM2>
            <uocXram2>0</uocXram2>
            <hadXRAM3>0</hadXRAM3>
            <ModC2>0</ModC2>
            <ModH2>0</ModH2>
            <Mdu_R515>0</Mdu_R515>
            <Mdu_F120>0</Mdu_F120>
            <Psoc>0</Psoc>
            <hadIROM2>0</hadIROM2>
            <hadIROM3>0</hadIROM3>
            <ModSmx2>0</ModSmx2>
            <cBanks>0</cBanks>
            <xBanks>0</xBanks>
            <OnChipMemories>
              <RCB>
                <Type>0</Type>
                <StartAddress>0x0</StartAddress>
                <Size>0x0</Size>
              </RCB>
              <RXB>
                <Type>0</Type>
                <StartAddress>0x0</StartAddress>
                <Size>0x0</Size>
              </RXB>
              <Ocm1>
                <Type>0</Type>
                <StartAddress>0x0</StartAddress>
                <Size>0x0</Size>
              </Ocm1>
              <Ocm2>
                <Type>0</Type>
                <StartAddress>0x0</StartAddress>
                <Size>0x0</Size>
              </Ocm2>
              <Ocm3>
                <Type>0</Type>
                <StartAddress>0x0</StartAddress>
                <Size>0x0</Size>
              </Ocm3>
              <Ocr1>
                <Type>0</Type>
                <StartAddress>0x0</StartAddress>
                <Size>0x0</Size>
              </Ocr1>
              <Ocr2>
                <Type>0</Type>
                <StartAddress>0x0</StartAddress>
                <Size>0x0</Size>
              </Ocr2>
              <Ocr3>
                <Type>0</Type>
                <StartAddress>0x0</StartAddress>
                <Size>0x0</Size>
              </Ocr3>
              <IRO>
                <Type>1</Type>
                <StartAddress>0x0</StartAddress>
                <Size>0x2000</Size>
              </IRO>
              <IRA>
                <Type>0</Type>
                <StartAddress>0x0</StartAddress>
                <Size>0x100</Size>
              </IRA>
              <XRA>
                <Type>0</Type>
                <StartAddress>0x0</StartAddress>
                <Size>0x0</Size>
              </XRA>
              <XRA512>
                <Type>0</Type>
                <StartAddress>0x0</StartAddress>
                <Size>0x0</Size>
              </XRA512>
              <IROM512>
                <Type>0</Type>
                <StartAddress>0x0</StartAddress>
                <Size>0x0</Size>
              </IROM512>
              <XRA513>
                <Type>0</Type>
                <StartAddress>0x0</StartAddress>
                <Size>0x0</Size>
              </XRA513>
              <IROM513>
                <Type>0</Type>
                <StartAddress>0x0</StartAddress>
                <Size>0x0</Size>
              </IROM513>
            </OnChipMemories>
          </Target51Misc>
          <C51>
            <RegisterColoring>0</RegisterColoring>
            <VariablesInOrder>0</VariablesInOrder>
            <IntegerPromotion>1</IntegerPromotion>
            <uAregs>0</uAregs>
            <UseInterruptVector>1</UseInterruptVector>
            <Fuzzy>3</Fuzzy>
            <Optimize>8</Optimize>
            <WarningLevel>2</WarningLevel>
            <SizeSpeed>1</SizeSpeed>
            <ObjectExtend>1</ObjectExtend>
            <ACallAJmp>0</ACallAJmp>
            <InterruptVectorAddress>0</InterruptVectorAddress>
            <VariousControls>
              <MiscControls></MiscControls>
              <Define></Define>
              <Undefine></Undefine>
              <IncludePath></IncludePath>
            </VariousControls>
          </C51>
          <Ax51>
            <UseMpl>0</UseMpl>
            <UseStandard>1</UseStandard>
            <UseCase>0</UseCase>
            <UseMod51>0</UseMod51>
            <VariousControls>
              <MiscControls></MiscControls>
              <Define></Define>
              <Undefine></Undefine>
              <IncludePath></IncludePath>
            </VariousControls>
          </Ax51>
          <Lx51>
            <useFile>0</useFile>
            <linkonly>0</linkonly>
            <UseMemoryFromTarget>1</UseMemoryFromTarget>
            <CaseSensitiveSymbols>0</CaseSensitiveSymbols>
            <WarningLevel>2</WarningLevel>
            <DataOverlaying>1</DataOverlaying>
            <OverlayString></OverlayString>
            <MiscControls></MiscControls>
            <DisableWarningNumbers></DisableWarningNumbers>
            <LinkerCmdFile></LinkerCmdFile>
            <Assign></Assign>
            <ReserveString></ReserveString>
            <CClasses></CClasses>
            <UserClasses></UserClasses>
            <CSection></CSection>
            <UserSection></UserSection>
            <CodeBaseAddress></CodeBaseAddress>
            <XDataBaseAddress></XDataBaseAddress>
            <PDataBaseAddress></PDataBaseAddress>
            <BitBaseAddress></BitBaseAddress>
            <DataBaseAddress></DataBaseAddress>
            <IDataBaseAddress></IDataBaseAddress>
            <Precede></Precede>
            <Stack></Stack>
            <CodeSegmentName></CodeSegmentName>
            <XDataSegmentName></XDataSegmentName>
            <BitSegmentName></BitSegmentName>
            <DataSegmentName></DataSegmentName>
            <IDataSegmentName></IDataSegmentName>
          </Lx51>
        </Target51>
      </TargetOption>
      <Groups>
        <Group>
          <GroupName>main</GroupName>
          <Files>
            <File>
              <FileName>he%d_%d.%s</FileName>
              <FileType>%d</FileType>
              <FilePath>..\\src\\he%d_%d.%s</FilePath>
            </File>
          </Files>
        </Group>
      </Groups>
    </Target>
  </Targets>

</Project>
'''
uvproj_t = '''
'''
uvproj_e = '''
'''
uvopt_s_dd_d_dds_dds = '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
<ProjectOpt xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="project_opt.xsd">

  <SchemaVersion>1.0</SchemaVersion>

  <Header>### uVision Project, (C) Keil Software</Header>

  <Extensions>
    <cExt>*.c</cExt>
    <aExt>*.s*; *.src; *.a*</aExt>
    <oExt>*.obj; *.o</oExt>
    <lExt>*.lib</lExt>
    <tExt>*.txt; *.h; *.inc</tExt>
    <pExt>*.plm</pExt>
    <CppX>*.cpp</CppX>
    <nMigrate>0</nMigrate>
  </Extensions>

  <DaveTm>
    <dwLowDateTime>0</dwLowDateTime>
    <dwHighDateTime>0</dwHighDateTime>
  </DaveTm>

  <Target>
    <TargetName>he%d_%d</TargetName>
    <ToolsetNumber>0x0</ToolsetNumber>
    <ToolsetName>MCS-51</ToolsetName>
    <TargetOption>
      <CLK51>24000000</CLK51>
      <OPTTT>
        <gFlags>0</gFlags>
        <BeepAtEnd>1</BeepAtEnd>
        <RunSim>1</RunSim>
        <RunTarget>0</RunTarget>
        <RunAbUc>0</RunAbUc>
      </OPTTT>
      <OPTHX>
        <HexSelection>0</HexSelection>
        <FlashByte>65535</FlashByte>
        <HexRangeLowAddress>0</HexRangeLowAddress>
        <HexRangeHighAddress>0</HexRangeHighAddress>
        <HexOffset>0</HexOffset>
      </OPTHX>
      <OPTLEX>
        <PageWidth>120</PageWidth>
        <PageLength>65</PageLength>
        <TabStop>8</TabStop>
        <ListingPath>.\\lst\\</ListingPath>
      </OPTLEX>
      <ListingPage>
        <CreateCListing>1</CreateCListing>
        <CreateAListing>1</CreateAListing>
        <CreateLListing>1</CreateLListing>
        <CreateIListing>0</CreateIListing>
        <AsmCond>1</AsmCond>
        <AsmSymb>1</AsmSymb>
        <AsmXref>0</AsmXref>
        <CCond>1</CCond>
        <CCode>0</CCode>
        <CListInc>0</CListInc>
        <CSymb>0</CSymb>
        <LinkerCodeListing>0</LinkerCodeListing>
      </ListingPage>
      <OPTXL>
        <LMap>1</LMap>
        <LComments>1</LComments>
        <LGenerateSymbols>1</LGenerateSymbols>
        <LLibSym>1</LLibSym>
        <LLines>1</LLines>
        <LLocSym>1</LLocSym>
        <LPubSym>1</LPubSym>
        <LXref>0</LXref>
        <LExpSel>0</LExpSel>
      </OPTXL>
      <OPTFL>
        <tvExp>1</tvExp>
        <tvExpOptDlg>0</tvExpOptDlg>
        <IsCurrentTarget>1</IsCurrentTarget>
      </OPTFL>
      <CpuCode>255</CpuCode>
      <Books>
        <Book>
          <Number>0</Number>
          <Title>Data Sheet</Title>
          <Path>DATASHTS\\ATMEL\\AT89C52_DS.PDF</Path>
        </Book>
        <Book>
          <Number>1</Number>
          <Title>Instruction Set Manual</Title>
          <Path>DATASHTS\\ATMEL\\AT_C51ISM.PDF</Path>
        </Book>
      </Books>
      <DebugOpt>
        <uSim>1</uSim>
        <uTrg>0</uTrg>
        <sLdApp>1</sLdApp>
        <sGomain>1</sGomain>
        <sRbreak>1</sRbreak>
        <sRwatch>1</sRwatch>
        <sRmem>1</sRmem>
        <sRfunc>1</sRfunc>
        <sRbox>1</sRbox>
        <tLdApp>1</tLdApp>
        <tGomain>0</tGomain>
        <tRbreak>1</tRbreak>
        <tRwatch>1</tRwatch>
        <tRmem>1</tRmem>
        <tRfunc>0</tRfunc>
        <tRbox>1</tRbox>
        <tRtrace>0</tRtrace>
        <sRSysVw>1</sRSysVw>
        <tRSysVw>1</tRSysVw>
        <sRunDeb>0</sRunDeb>
        <sLrtime>0</sLrtime>
        <bEvRecOn>1</bEvRecOn>
        <bSchkAxf>0</bSchkAxf>
        <bTchkAxf>0</bTchkAxf>
        <nTsel>-1</nTsel>
        <sDll></sDll>
        <sDllPa></sDllPa>
        <sDlgDll></sDlgDll>
        <sDlgPa></sDlgPa>
        <sIfile></sIfile>
        <tDll></tDll>
        <tDllPa></tDllPa>
        <tDlgDll></tDlgDll>
        <tDlgPa></tDlgPa>
        <tIfile></tIfile>
        <pMon></pMon>
      </DebugOpt>
      <TargetDriverDllRegistry>
        <SetRegEntry>
          <Number>0</Number>
          <Key>DLGDP51</Key>
          <Name>(98=-1,-1,-1,-1,0)(82=-1,-1,-1,-1,0)(83=-1,-1,-1,-1,0)(84=-1,-1,-1,-1,0)(85=-1,-1,-1,-1,0)(99=-1,-1,-1,-1,0)(91=-1,-1,-1,-1,0)(92=-1,-1,-1,-1,0)(93=-1,-1,-1,-1,0)</Name>
        </SetRegEntry>
      </TargetDriverDllRegistry>
      <Breakpoint/>
      <MemoryWindow1>
        <Mm>
          <WinNumber>1</WinNumber>
          <SubType>0</SubType>
          <ItemText>d:00h</ItemText>
          <AccSizeX>0</AccSizeX>
        </Mm>
      </MemoryWindow1>
      <MemoryWindow2>
        <Mm>
          <WinNumber>2</WinNumber>
          <SubType>0</SubType>
          <ItemText>i:00h</ItemText>
          <AccSizeX>0</AccSizeX>
        </Mm>
      </MemoryWindow2>
      <MemoryWindow3>
        <Mm>
          <WinNumber>3</WinNumber>
          <SubType>0</SubType>
          <ItemText>x:0000h</ItemText>
          <AccSizeX>0</AccSizeX>
        </Mm>
      </MemoryWindow3>
      <Tracepoint>
        <THDelay>0</THDelay>
      </Tracepoint>
      <DebugFlag>
        <trace>0</trace>
        <periodic>1</periodic>
        <aLwin>1</aLwin>
        <aCover>0</aCover>
        <aSer1>0</aSer1>
        <aSer2>0</aSer2>
        <aPa>0</aPa>
        <viewmode>1</viewmode>
        <vrSel>0</vrSel>
        <aSym>0</aSym>
        <aTbox>0</aTbox>
        <AscS1>0</AscS1>
        <AscS2>0</AscS2>
        <AscS3>0</AscS3>
        <aSer3>0</aSer3>
        <eProf>0</eProf>
        <aLa>0</aLa>
        <aPa1>0</aPa1>
        <AscS4>0</AscS4>
        <aSer4>0</aSer4>
        <StkLoc>0</StkLoc>
        <TrcWin>0</TrcWin>
        <newCpu>0</newCpu>
        <uProt>0</uProt>
      </DebugFlag>
      <LintExecutable></LintExecutable>
      <LintConfigFile></LintConfigFile>
      <bLintAuto>0</bLintAuto>
      <bAutoGenD>0</bAutoGenD>
      <LntExFlags>0</LntExFlags>
      <pMisraName></pMisraName>
      <pszMrule></pszMrule>
      <pSingCmds></pSingCmds>
      <pMultCmds></pMultCmds>
      <pMisraNamep></pMisraNamep>
      <pszMrulep></pszMrulep>
      <pSingCmdsp></pSingCmdsp>
      <pMultCmdsp></pMultCmdsp>
    </TargetOption>
  </Target>

  <Group>
    <GroupName>main</GroupName>
    <tvExp>1</tvExp>
    <tvExpOptDlg>0</tvExpOptDlg>
    <cbSel>0</cbSel>
    <RteFlg>0</RteFlg>
    <File>
      <GroupNumber>1</GroupNumber>
      <FileNumber>1</FileNumber>
      <FileType>%d</FileType>
      <tvExp>0</tvExp>
      <tvExpOptDlg>0</tvExpOptDlg>
      <bDave2>0</bDave2>
      <PathWithFileName>..\\src\\he%d_%d.%s</PathWithFileName>
      <FilenameWithoutPath>he%d_%d.%s</FilenameWithoutPath>
      <RteFlg>0</RteFlg>
      <bShared>0</bShared>
    </File>
  </Group>

</ProjectOpt>
'''
uvopt_t = '''
'''
uvopt_e = '''
'''

num_class = len(num_subclass)
# open files
root_dir = "./HE"+str(SE_no)+"/"
os.mkdir(path=root_dir)
uvmpw = open(root_dir+"HE"+str(SE_no)+".uvmpw", mode="w")
uvmpw.write(multi_s0)

# write to multi-proj file
for i in range(1, 1+num_class):
    for j in range(1, 1+num_subclass[i-1]):
        uvmpw.write(multi_t_dd % (i, j))
        uvmpw.flush()
uvmpw.write(multi_e0)
uvmpw.flush()
uvmpw.close()

# create sub dirs
src_dir = root_dir+"src/"
sub_dir = root_dir+"sub_prjs/"
os.mkdir(path=src_dir)
os.mkdir(path=sub_dir)

# write to sub single-proj files
for i in range(1, 1+num_class):
    for j in range(1, 1+num_subclass[i-1]):
        tmp = open(sub_dir+"HE%d_%d.uvproj" % (i, j), mode="w")
        tmp.write(uvproj_s_dd_dds_d_dds %
                  (i, j, i, j, filetype, typelist[filetype], i, j, filetype))
        tmp.flush()
        tmp.close()

# write to sub single-opt files
for i in range(1, 1+num_class):
    for j in range(1, 1+num_subclass[i-1]):
        tmp = open(sub_dir+"HE%d_%d.uvopt" % (i, j), mode="w")
        tmp.write(uvopt_s_dd_d_dds_dds %
                  (i, j, typelist[filetype], i, j, filetype, i, j, filetype))
        tmp.flush()
        tmp.close()

# create template src files
for i in range(1, 1+num_class):
    for j in range(1, 1+num_subclass[i-1]):
        tmp = open(src_dir+"he%d_%d.%s" % (i, j, filetype), mode="w")
        tmp.write(typetemplates[filetype])
        tmp.close()
