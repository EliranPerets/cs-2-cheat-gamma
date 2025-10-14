class ActiveModelConfig_t:
    m_Handle = 0x30  # ModelConfigHandle_t
    m_Name = 0x38  # string_t
    m_AssociatedEntities = 0x40  # CHandle<C_BaseModelEntity>
    m_AssociatedEntityNames = 0x58  # string_t
    pass

class CAnimGraphNetworkedVariables:
    m_PredNetBoolVariables = 0x8  # unknown_t
    m_PredNetByteVariables = 0x20  # unknown_t
    m_PredNetUInt16Variables = 0x38  # unknown_t
    m_PredNetIntVariables = 0x50  # unknown_t
    m_PredNetUInt32Variables = 0x68  # unknown_t
    m_PredNetUInt64Variables = 0x80  # unknown_t
    m_PredNetFloatVariables = 0x98  # unknown_t
    m_PredNetVectorVariables = 0xB0  # unknown_t
    m_PredNetQuaternionVariables = 0xC8  # unknown_t
    m_PredNetGlobalSymbolVariables = 0xE0  # unknown_t
    m_OwnerOnlyPredNetBoolVariables = 0xF8  # unknown_t
    m_OwnerOnlyPredNetByteVariables = 0x110  # unknown_t
    m_OwnerOnlyPredNetUInt16Variables = 0x128  # unknown_t
    m_OwnerOnlyPredNetIntVariables = 0x140  # unknown_t
    m_OwnerOnlyPredNetUInt32Variables = 0x158  # unknown_t
    m_OwnerOnlyPredNetUInt64Variables = 0x170  # unknown_t
    m_OwnerOnlyPredNetFloatVariables = 0x188  # unknown_t
    m_OwnerOnlyPredNetVectorVariables = 0x1A0  # unknown_t
    m_OwnerOnlyPredNetQuaternionVariables = 0x1B8  # unknown_t
    m_OwnerOnlyPredNetGlobalSymbolVariables = 0x1D0  # unknown_t
    m_nBoolVariablesCount = 0x1E8  # unknown_t
    m_nOwnerOnlyBoolVariablesCount = 0x1EC  # unknown_t
    m_nRandomSeedOffset = 0x1F0  # unknown_t
    m_flLastTeleportTime = 0x1F4  # unknown_t
    pass

class CAttributeList:
    m_Attributes = 0x8  # unknown_t
    m_pManager = 0x70  # unknown_t
    pass

class CAttributeManager:
    m_Providers = 0x8  # unknown_t
    m_iReapplyProvisionParity = 0x20  # unknown_t
    m_hOuter = 0x24  # unknown_t
    m_bPreventLoopback = 0x28  # unknown_t
    m_ProviderType = 0x2C  # unknown_t
    m_CachedResults = 0x30  # unknown_t
    pass

class CAttributeManager__cached_attribute_float_t:
    flIn = 0x0  # unknown_t
    iAttribHook = 0x8  # unknown_t
    flOut = 0x10  # unknown_t
    pass

class CBaseAnimGraph:
    m_bInitiallyPopulateInterpHistory = 0xF48  # unknown_t
    m_bSuppressAnimEventSounds = 0xF4A  # unknown_t
    m_bAnimGraphUpdateEnabled = 0xF58  # unknown_t
    m_flMaxSlopeDistance = 0xF5C  # unknown_t
    m_vLastSlopeCheckPos = 0xF60  # unknown_t
    m_bAnimationUpdateScheduled = 0xF6C  # unknown_t
    m_vecForce = 0xF70  # unknown_t
    m_nForceBone = 0xF7C  # unknown_t
    m_pClientsideRagdoll = 0xF80  # unknown_t
    m_bBuiltRagdoll = 0xF88  # unknown_t
    m_RagdollPose = 0xFA0  # unknown_t
    m_bRagdollEnabled = 0xFE8  # unknown_t
    m_bRagdollClientSide = 0xFE9  # unknown_t
    m_bHasAnimatedMaterialAttributes = 0xFF8  # unknown_t
    pass

class CBaseAnimGraphController:
    m_animGraphNetworkedVars = 0x18  # unknown_t
    m_bSequenceFinished = 0x14A8  # unknown_t
    m_flSoundSyncTime = 0x14AC  # unknown_t
    m_nActiveIKChainMask = 0x14B0  # unknown_t
    m_hSequence = 0x14B4  # unknown_t
    m_flSeqStartTime = 0x14B8  # unknown_t
    m_flSeqFixedCycle = 0x14BC  # unknown_t
    m_nAnimLoopMode = 0x14C0  # unknown_t
    m_flPlaybackRate = 0x14C4  # unknown_t
    m_nNotifyState = 0x14D0  # unknown_t
    m_bNetworkedAnimationInputsChanged = 0x14D2  # unknown_t
    m_bNetworkedSequenceChanged = 0x14D3  # unknown_t
    m_bLastUpdateSkipped = 0x14D4  # unknown_t
    m_flPrevAnimUpdateTime = 0x14D8  # unknown_t
    m_hGraphDefinitionAG2 = 0x1860  # unknown_t
    m_bIsUsingAG2 = 0x1868  # unknown_t
    m_serializedPoseRecipeAG2 = 0x1870  # unknown_t
    m_nSerializePoseRecipeSizeAG2 = 0x1888  # unknown_t
    m_nSerializePoseRecipeVersionAG2 = 0x188C  # unknown_t
    m_nGraphCreationFlagsAG2 = 0x1890  # unknown_t
    m_nServerGraphDefReloadCountAG2 = 0x18D4  # unknown_t
    pass

class CBaseFilter:
    m_bNegated = 0x5F8  # unknown_t
    m_OnPass = 0x600  # unknown_t
    m_OnFail = 0x628  # unknown_t
    pass

class CBasePlayerController:
    m_CommandContext = 0x600  # unknown_t
    m_nInButtonsWhichAreToggles = 0x6A8  # unknown_t
    m_nTickBase = 0x6B0  # unknown_t
    m_hPawn = 0x6B4  # unknown_t
    m_bKnownTeamMismatch = 0x6B8  # unknown_t
    m_hPredictedPawn = 0x6BC  # unknown_t
    m_nSplitScreenSlot = 0x6C0  # unknown_t
    m_hSplitOwner = 0x6C4  # unknown_t
    m_hSplitScreenPlayers = 0x6C8  # unknown_t
    m_bIsHLTV = 0x6E0  # unknown_t
    m_iConnected = 0x6E4  # unknown_t
    m_iszPlayerName = 0x6E8  # string_t
    m_steamID = 0x770  # unknown_t
    m_bIsLocalPlayerController = 0x778  # unknown_t
    m_bNoClipEnabled = 0x779  # unknown_t
    m_iDesiredFOV = 0x77C  # unknown_t
    pass

class CBasePlayerControllerAPI:
    pass

class CBasePlayerVData:
    m_sModelName = 0x28  # string_t
    m_flHeadDamageMultiplier = 0x108  # unknown_t
    m_flChestDamageMultiplier = 0x118  # unknown_t
    m_flStomachDamageMultiplier = 0x128  # unknown_t
    m_flArmDamageMultiplier = 0x138  # unknown_t
    m_flLegDamageMultiplier = 0x148  # unknown_t
    m_flHoldBreathTime = 0x158  # unknown_t
    m_flDrowningDamageInterval = 0x15C  # unknown_t
    m_nDrowningDamageInitial = 0x160  # unknown_t
    m_nDrowningDamageMax = 0x164  # unknown_t
    m_nWaterSpeed = 0x168  # unknown_t
    m_flUseRange = 0x16C  # unknown_t
    m_flUseAngleTolerance = 0x170  # unknown_t
    m_flCrouchTime = 0x174  # unknown_t
    pass

class CBasePlayerWeaponVData:
    m_szWorldModel = 0x28  # unknown_t
    m_sToolsOnlyOwnerModelName = 0x108  # string_t
    m_bBuiltRightHanded = 0x1E8  # unknown_t
    m_bAllowFlipping = 0x1E9  # unknown_t
    m_sMuzzleAttachment = 0x1F0  # unknown_t
    m_szMuzzleFlashParticle = 0x210  # unknown_t
    m_szMuzzleFlashParticleConfig = 0x2F0  # unknown_t
    m_szBarrelSmokeParticle = 0x2F8  # unknown_t
    m_nMuzzleSmokeShotThreshold = 0x3D8  # unknown_t
    m_flMuzzleSmokeTimeout = 0x3DC  # unknown_t
    m_flMuzzleSmokeDecrementRate = 0x3E0  # unknown_t
    m_bLinkedCooldowns = 0x3E4  # unknown_t
    m_iFlags = 0x3E5  # unknown_t
    m_nPrimaryAmmoType = 0x3E6  # unknown_t
    m_nSecondaryAmmoType = 0x3E7  # unknown_t
    m_iMaxClip1 = 0x3E8  # unknown_t
    m_iMaxClip2 = 0x3EC  # unknown_t
    m_iDefaultClip1 = 0x3F0  # unknown_t
    m_iDefaultClip2 = 0x3F4  # unknown_t
    m_bReserveAmmoAsClips = 0x3F8  # unknown_t
    m_bTreatAsSingleClip = 0x3F9  # unknown_t
    m_iWeight = 0x3FC  # unknown_t
    m_bAutoSwitchTo = 0x400  # unknown_t
    m_bAutoSwitchFrom = 0x401  # unknown_t
    m_iRumbleEffect = 0x404  # unknown_t
    m_flDropSpeed = 0x408  # unknown_t
    m_iSlot = 0x40C  # unknown_t
    m_iPosition = 0x410  # unknown_t
    m_aShootSounds = 0x418  # unknown_t
    pass

class CBaseProp:
    m_bModelOverrodeBlockLOS = 0x1170  # unknown_t
    m_iShapeType = 0x1174  # unknown_t
    m_bConformToCollisionBounds = 0x1178  # unknown_t
    m_mPreferredCatchTransform = 0x1180  # unknown_t
    pass

class CBasePulseGraphInstance:
    pass

class CBaseTriggerAPI:
    pass

class CBodyComponent:
    m_pSceneNode = 0x8  # unknown_t
    __m_pChainEntity = 0x48  # unknown_t
    pass

class CBodyComponentBaseAnimGraph:
    m_animationController = 0x5B0  # unknown_t
    pass

class CBodyComponentBaseModelEntity:
    pass

class CBodyComponentPoint:
    m_sceneNode = 0x80  # unknown_t
    pass

class CBodyComponentSkeletonInstance:
    m_skeletonInstance = 0x80  # unknown_t
    pass

class CBombTarget:
    m_bBombPlantedHere = 0x1008  # unknown_t
    pass

class CBuoyancyHelper:
    m_nFluidType = 0x18  # unknown_t
    m_flFluidDensity = 0x1C  # unknown_t
    m_flNeutrallyBuoyantGravity = 0x20  # unknown_t
    m_flNeutrallyBuoyantLinearDamping = 0x24  # unknown_t
    m_flNeutrallyBuoyantAngularDamping = 0x28  # unknown_t
    m_bNeutrallyBuoyant = 0x2C  # unknown_t
    m_vecFractionOfWheelSubmergedForWheelFriction = 0x30  # unknown_t
    m_vecWheelFrictionScales = 0x48  # unknown_t
    m_vecFractionOfWheelSubmergedForWheelDrag = 0x60  # unknown_t
    m_vecWheelDrag = 0x78  # unknown_t
    pass

class CCSGO_WingmanIntroCharacterPosition:
    pass

class CCSGO_WingmanIntroCounterTerroristPosition:
    pass

class CCSGO_WingmanIntroTerroristPosition:
    pass

class CCSGameModeRules:
    __m_pChainEntity = 0x8  # unknown_t
    pass

class CCSGameModeRules_ArmsRace:
    m_WeaponSequence = 0x30  # unknown_t
    pass

class CCSGameModeRules_Deathmatch:
    m_flDMBonusStartTime = 0x30  # unknown_t
    m_flDMBonusTimeLength = 0x34  # unknown_t
    m_sDMBonusWeapon = 0x38  # unknown_t
    pass

class CCSGameModeRules_Noop:
    pass

class CCSObserver_CameraServices:
    pass

class CCSObserver_MovementServices:
    pass

class CCSObserver_ObserverServices:
    m_obsInterpState = 0x5C  # unknown_t
    pass

class CCSObserver_UseServices:
    pass

class CCSPlayerBase_CameraServices:
    m_iFOV = 0x288  # unknown_t
    m_iFOVStart = 0x28C  # unknown_t
    m_flFOVTime = 0x290  # unknown_t
    m_flFOVRate = 0x294  # unknown_t
    m_hZoomOwner = 0x298  # unknown_t
    m_flLastShotFOV = 0x29C  # unknown_t
    pass

class CCSPlayerController:
    m_pInGameMoneyServices = 0x7F8  # unknown_t
    m_pInventoryServices = 0x800  # unknown_t
    m_pActionTrackingServices = 0x808  # unknown_t
    m_pDamageServices = 0x810  # unknown_t
    m_iPing = 0x818  # unknown_t
    m_bHasCommunicationAbuseMute = 0x81C  # unknown_t
    m_uiCommunicationMuteFlags = 0x820  # unknown_t
    m_szCrosshairCodes = 0x828  # unknown_t
    m_iPendingTeamNum = 0x830  # unknown_t
    m_flForceTeamTime = 0x834  # unknown_t
    m_iCompTeammateColor = 0x838  # unknown_t
    m_bEverPlayedOnTeam = 0x83C  # unknown_t
    m_flPreviousForceJoinTeamTime = 0x840  # unknown_t
    m_szClan = 0x848  # unknown_t
    m_sSanitizedPlayerName = 0x850  # string_t
    m_iCoachingTeam = 0x858  # unknown_t
    m_nPlayerDominated = 0x860  # unknown_t
    m_nPlayerDominatingMe = 0x868  # unknown_t
    m_iCompetitiveRanking = 0x870  # unknown_t
    m_iCompetitiveWins = 0x874  # unknown_t
    m_iCompetitiveRankType = 0x878  # unknown_t
    m_iCompetitiveRankingPredicted_Win = 0x87C  # unknown_t
    m_iCompetitiveRankingPredicted_Loss = 0x880  # unknown_t
    m_iCompetitiveRankingPredicted_Tie = 0x884  # unknown_t
    m_nEndMatchNextMapVote = 0x888  # unknown_t
    m_unActiveQuestId = 0x88C  # unknown_t
    m_rtActiveMissionPeriod = 0x890  # unknown_t
    m_nQuestProgressReason = 0x894  # unknown_t
    m_unPlayerTvControlFlags = 0x898  # unknown_t
    m_iDraftIndex = 0x8C8  # unknown_t
    m_msQueuedModeDisconnectionTimestamp = 0x8CC  # unknown_t
    m_uiAbandonRecordedReason = 0x8D0  # unknown_t
    m_eNetworkDisconnectionReason = 0x8D4  # unknown_t
    m_bCannotBeKicked = 0x8D8  # unknown_t
    m_bEverFullyConnected = 0x8D9  # unknown_t
    m_bAbandonAllowsSurrender = 0x8DA  # unknown_t
    m_bAbandonOffersInstantSurrender = 0x8DB  # unknown_t
    m_bDisconnection1MinWarningPrinted = 0x8DC  # unknown_t
    m_bScoreReported = 0x8DD  # unknown_t
    m_nDisconnectionTick = 0x8E0  # unknown_t
    m_bControllingBot = 0x8F0  # unknown_t
    m_bHasControlledBotThisRound = 0x8F1  # unknown_t
    m_bHasBeenControlledByPlayerThisRound = 0x8F2  # unknown_t
    m_nBotsControlledThisRound = 0x8F4  # unknown_t
    m_bCanControlObservedBot = 0x8F8  # unknown_t
    m_hPlayerPawn = 0x8FC  # unknown_t
    m_hObserverPawn = 0x900  # unknown_t
    m_bPawnIsAlive = 0x904  # unknown_t
    m_iPawnHealth = 0x908  # unknown_t
    m_iPawnArmor = 0x90C  # unknown_t
    m_bPawnHasDefuser = 0x910  # unknown_t
    m_bPawnHasHelmet = 0x911  # unknown_t
    m_nPawnCharacterDefIndex = 0x912  # unknown_t
    m_iPawnLifetimeStart = 0x914  # unknown_t
    m_iPawnLifetimeEnd = 0x918  # unknown_t
    m_iPawnBotDifficulty = 0x91C  # unknown_t
    m_hOriginalControllerOfCurrentPawn = 0x920  # unknown_t
    m_iScore = 0x924  # unknown_t
    m_recentKillQueue = 0x928  # unknown_t
    m_nFirstKill = 0x930  # unknown_t
    m_nKillCount = 0x931  # unknown_t
    m_bMvpNoMusic = 0x932  # unknown_t
    m_eMvpReason = 0x934  # unknown_t
    m_iMusicKitID = 0x938  # unknown_t
    m_iMusicKitMVPs = 0x93C  # unknown_t
    m_iMVPs = 0x940  # unknown_t
    m_bIsPlayerNameDirty = 0x944  # string_t
    m_bFireBulletsSeedSynchronized = 0x945  # unknown_t
    pass

class CCSPlayerController_ActionTrackingServices:
    m_perRoundStats = 0x40  # unknown_t
    m_matchStats = 0xA8  # unknown_t
    m_iNumRoundKills = 0x128  # unknown_t
    m_iNumRoundKillsHeadshots = 0x12C  # unknown_t
    m_flTotalRoundDamageDealt = 0x130  # unknown_t
    pass

class CCSPlayerController_DamageServices:
    m_nSendUpdate = 0x40  # unknown_t
    m_DamageList = 0x48  # unknown_t
    pass

class CCSPlayerController_InGameMoneyServices:
    m_iAccount = 0x40  # unknown_t
    m_iStartAccount = 0x44  # unknown_t
    m_iTotalCashSpent = 0x48  # unknown_t
    m_iCashSpentThisRound = 0x4C  # unknown_t
    pass

class CCSPlayerController_InventoryServices:
    m_vecNetworkableLoadout = 0x40  # unknown_t
    m_unMusicID = 0x58  # unknown_t
    m_rank = 0x5C  # unknown_t
    m_nPersonaDataPublicLevel = 0x74  # unknown_t
    m_nPersonaDataPublicCommendsLeader = 0x78  # unknown_t
    m_nPersonaDataPublicCommendsTeacher = 0x7C  # unknown_t
    m_nPersonaDataPublicCommendsFriendly = 0x80  # unknown_t
    m_nPersonaDataXpTrailLevel = 0x84  # unknown_t
    m_vecServerAuthoritativeWeaponSlots = 0x88  # unknown_t
    pass

class CCSPlayerController_InventoryServices__NetworkedLoadoutSlot_t:
    pItem = 0x0  # unknown_t
    team = 0x8  # unknown_t
    slot = 0xA  # unknown_t
    pass

class CCSPlayer_ActionTrackingServices:
    m_hLastWeaponBeforeC4AutoSwitch = 0x40  # unknown_t
    m_bIsRescuing = 0x44  # unknown_t
    m_weaponPurchasesThisMatch = 0x48  # unknown_t
    m_weaponPurchasesThisRound = 0xB8  # unknown_t
    pass

class CCSPlayer_BulletServices:
    m_totalHitsOnServer = 0x40  # unknown_t
    pass

class CCSPlayer_BuyServices:
    m_vecSellbackPurchaseEntries = 0x40  # unknown_t
    pass

class CCSPlayer_CameraServices:
    m_flDeathCamTilt = 0x2A0  # unknown_t
    m_vClientScopeInaccuracy = 0x2A8  # unknown_t
    pass

class CCSPlayer_DamageReactServices:
    pass

class CCSPlayer_GlowServices:
    pass

class CCSPlayer_HostageServices:
    m_hCarriedHostage = 0x40  # unknown_t
    m_hCarriedHostageProp = 0x44  # unknown_t
    pass

class CCSPlayer_ItemServices:
    m_bHasDefuser = 0x40  # unknown_t
    m_bHasHelmet = 0x41  # unknown_t
    pass

class CCSPlayer_MovementServices:
    m_vecLadderNormal = 0x278  # unknown_t
    m_nLadderSurfacePropIndex = 0x284  # unknown_t
    m_flDuckAmount = 0x288  # unknown_t
    m_flDuckSpeed = 0x28C  # unknown_t
    m_bDuckOverride = 0x290  # unknown_t
    m_bDesiresDuck = 0x291  # unknown_t
    m_flDuckOffset = 0x294  # unknown_t
    m_nDuckTimeMsecs = 0x298  # unknown_t
    m_nDuckJumpTimeMsecs = 0x29C  # unknown_t
    m_nJumpTimeMsecs = 0x2A0  # unknown_t
    m_flLastDuckTime = 0x2A4  # unknown_t
    m_vecLastPositionAtFullCrouchSpeed = 0x2B0  # unknown_t
    m_duckUntilOnGround = 0x2B8  # unknown_t
    m_bHasWalkMovedSinceLastJump = 0x2B9  # unknown_t
    m_bInStuckTest = 0x2BA  # unknown_t
    m_nTraceCount = 0x4C8  # unknown_t
    m_StuckLast = 0x4CC  # unknown_t
    m_bSpeedCropped = 0x4D0  # unknown_t
    m_nOldWaterLevel = 0x4D4  # unknown_t
    m_flWaterEntryTime = 0x4D8  # unknown_t
    m_vecForward = 0x4DC  # unknown_t
    m_vecLeft = 0x4E8  # unknown_t
    m_vecUp = 0x4F4  # unknown_t
    m_nGameCodeHasMovedPlayerAfterCommand = 0x500  # unknown_t
    m_bOldJumpPressed = 0x504  # unknown_t
    m_flJumpPressedTime = 0x508  # unknown_t
    m_fStashGrenadeParameterWhen = 0x50C  # unknown_t
    m_nButtonDownMaskPrev = 0x510  # unknown_t
    m_flOffsetTickCompleteTime = 0x518  # unknown_t
    m_flOffsetTickStashedSpeed = 0x51C  # unknown_t
    m_flStamina = 0x520  # unknown_t
    m_flHeightAtJumpStart = 0x524  # unknown_t
    m_flMaxJumpHeightThisJump = 0x528  # unknown_t
    m_flMaxJumpHeightLastJump = 0x52C  # unknown_t
    m_flStaminaAtJumpStart = 0x530  # unknown_t
    m_flAccumulatedJumpError = 0x534  # unknown_t
    m_flTicksSinceLastSurfingDetected = 0x538  # unknown_t
    m_bWasSurfing = 0x53C  # unknown_t
    m_vecInputRotated = 0x5CC  # unknown_t
    pass

class CCSPlayer_PingServices:
    m_hPlayerPing = 0x40  # unknown_t
    pass

class CCSPlayer_UseServices:
    pass

class CCSPlayer_WaterServices:
    m_flWaterJumpTime = 0x40  # unknown_t
    m_vecWaterJumpVel = 0x44  # unknown_t
    m_flSwimSoundTime = 0x50  # unknown_t
    pass

class CCSPlayer_WeaponServices:
    m_flNextAttack = 0xC8  # unknown_t
    m_bIsLookingAtWeapon = 0xCC  # unknown_t
    m_bIsHoldingLookAtWeapon = 0xCD  # unknown_t
    m_nOldTotalShootPositionHistoryCount = 0xD0  # unknown_t
    m_nOldTotalInputHistoryCount = 0x368  # unknown_t
    m_networkAnimTiming = 0x18C8  # unknown_t
    m_bBlockInspectUntilNextGraphUpdate = 0x18E0  # unknown_t
    pass

class CCSPointScriptEntity:
    pass

class CCSWeaponBaseVData:
    m_WeaponType = 0x440  # unknown_t
    m_WeaponCategory = 0x444  # unknown_t
    m_szModel_AG2 = 0x448  # unknown_t
    m_szAnimSkeleton = 0x528  # unknown_t
    m_vecMuzzlePos0 = 0x608  # unknown_t
    m_vecMuzzlePos1 = 0x614  # unknown_t
    m_szTracerParticle = 0x620  # unknown_t
    m_GearSlot = 0x700  # unknown_t
    m_GearSlotPosition = 0x704  # unknown_t
    m_DefaultLoadoutSlot = 0x708  # unknown_t
    m_nPrice = 0x70C  # unknown_t
    m_nKillAward = 0x710  # unknown_t
    m_nPrimaryReserveAmmoMax = 0x714  # unknown_t
    m_nSecondaryReserveAmmoMax = 0x718  # unknown_t
    m_bMeleeWeapon = 0x71C  # unknown_t
    m_bHasBurstMode = 0x71D  # unknown_t
    m_bIsRevolver = 0x71E  # unknown_t
    m_bCannotShootUnderwater = 0x71F  # unknown_t
    m_szName = 0x720  # string_t
    m_eSilencerType = 0x728  # unknown_t
    m_nCrosshairMinDistance = 0x72C  # unknown_t
    m_nCrosshairDeltaDistance = 0x730  # unknown_t
    m_bIsFullAuto = 0x734  # unknown_t
    m_nNumBullets = 0x738  # unknown_t
    m_bReloadsSingleShells = 0x73C  # unknown_t
    m_flCycleTime = 0x740  # unknown_t
    m_flMaxSpeed = 0x748  # unknown_t
    m_flSpread = 0x750  # unknown_t
    m_flInaccuracyCrouch = 0x758  # unknown_t
    m_flInaccuracyStand = 0x760  # unknown_t
    m_flInaccuracyJump = 0x768  # unknown_t
    m_flInaccuracyLand = 0x770  # unknown_t
    m_flInaccuracyLadder = 0x778  # unknown_t
    m_flInaccuracyFire = 0x780  # unknown_t
    m_flInaccuracyMove = 0x788  # unknown_t
    m_flRecoilAngle = 0x790  # unknown_t
    m_flRecoilAngleVariance = 0x798  # unknown_t
    m_flRecoilMagnitude = 0x7A0  # unknown_t
    m_flRecoilMagnitudeVariance = 0x7A8  # unknown_t
    m_nTracerFrequency = 0x7B0  # unknown_t
    m_flInaccuracyJumpInitial = 0x7B8  # unknown_t
    m_flInaccuracyJumpApex = 0x7BC  # unknown_t
    m_flInaccuracyReload = 0x7C0  # unknown_t
    m_flDeployDuration = 0x7C4  # unknown_t
    m_flDisallowAttackAfterReloadStartDuration = 0x7C8  # unknown_t
    m_nRecoilSeed = 0x7CC  # unknown_t
    m_nSpreadSeed = 0x7D0  # unknown_t
    m_flAttackMovespeedFactor = 0x7D4  # unknown_t
    m_flInaccuracyPitchShift = 0x7D8  # unknown_t
    m_flInaccuracyAltSoundThreshold = 0x7DC  # unknown_t
    m_szUseRadioSubtitle = 0x7E0  # unknown_t
    m_bUnzoomsAfterShot = 0x7E8  # unknown_t
    m_bHideViewModelWhenZoomed = 0x7E9  # unknown_t
    m_nZoomLevels = 0x7EC  # unknown_t
    m_nZoomFOV1 = 0x7F0  # unknown_t
    m_nZoomFOV2 = 0x7F4  # unknown_t
    m_flZoomTime0 = 0x7F8  # unknown_t
    m_flZoomTime1 = 0x7FC  # unknown_t
    m_flZoomTime2 = 0x800  # unknown_t
    m_flIronSightPullUpSpeed = 0x804  # unknown_t
    m_flIronSightPutDownSpeed = 0x808  # unknown_t
    m_flIronSightFOV = 0x80C  # unknown_t
    m_flIronSightPivotForward = 0x810  # unknown_t
    m_flIronSightLooseness = 0x814  # unknown_t
    m_nDamage = 0x818  # unknown_t
    m_flHeadshotMultiplier = 0x81C  # unknown_t
    m_flArmorRatio = 0x820  # unknown_t
    m_flPenetration = 0x824  # unknown_t
    m_flRange = 0x828  # unknown_t
    m_flRangeModifier = 0x82C  # unknown_t
    m_flFlinchVelocityModifierLarge = 0x830  # unknown_t
    m_flFlinchVelocityModifierSmall = 0x834  # unknown_t
    m_flRecoveryTimeCrouch = 0x838  # unknown_t
    m_flRecoveryTimeStand = 0x83C  # unknown_t
    m_flRecoveryTimeCrouchFinal = 0x840  # unknown_t
    m_flRecoveryTimeStandFinal = 0x844  # unknown_t
    m_nRecoveryTransitionStartBullet = 0x848  # unknown_t
    m_nRecoveryTransitionEndBullet = 0x84C  # unknown_t
    m_flThrowVelocity = 0x850  # unknown_t
    m_vSmokeColor = 0x854  # unknown_t
    m_szAnimClass = 0x860  # unknown_t
    pass

class CCS_PortraitWorldCallbackHandler:
    pass

class CCitadelSoundOpvarSetOBB:
    m_iszStackName = 0x610  # string_t
    m_iszOperatorName = 0x618  # string_t
    m_iszOpvarName = 0x620  # string_t
    m_vDistanceInnerMins = 0x628  # unknown_t
    m_vDistanceInnerMaxs = 0x634  # unknown_t
    m_vDistanceOuterMins = 0x640  # unknown_t
    m_vDistanceOuterMaxs = 0x64C  # unknown_t
    m_nAABBDirection = 0x658  # unknown_t
    pass

class CCollisionProperty:
    m_collisionAttribute = 0x10  # unknown_t
    m_vecMins = 0x40  # unknown_t
    m_vecMaxs = 0x4C  # unknown_t
    m_usSolidFlags = 0x5A  # unknown_t
    m_nSolidType = 0x5B  # unknown_t
    m_triggerBloat = 0x5C  # unknown_t
    m_nSurroundType = 0x5D  # unknown_t
    m_CollisionGroup = 0x5E  # unknown_t
    m_nEnablePhysics = 0x5F  # unknown_t
    m_flBoundingRadius = 0x60  # unknown_t
    m_vecSpecifiedSurroundingMins = 0x64  # unknown_t
    m_vecSpecifiedSurroundingMaxs = 0x70  # unknown_t
    m_vecSurroundingMaxs = 0x7C  # unknown_t
    m_vecSurroundingMins = 0x88  # unknown_t
    m_vCapsuleCenter1 = 0x94  # unknown_t
    m_vCapsuleCenter2 = 0xA0  # unknown_t
    m_flCapsuleRadius = 0xAC  # unknown_t
    pass

class CDamageRecord:
    m_PlayerDamager = 0x30  # unknown_t
    m_PlayerRecipient = 0x34  # unknown_t
    m_hPlayerControllerDamager = 0x38  # unknown_t
    m_hPlayerControllerRecipient = 0x3C  # unknown_t
    m_szPlayerDamagerName = 0x40  # string_t
    m_szPlayerRecipientName = 0x48  # string_t
    m_DamagerXuid = 0x50  # unknown_t
    m_RecipientXuid = 0x58  # unknown_t
    m_flBulletsDamage = 0x60  # unknown_t
    m_flDamage = 0x64  # unknown_t
    m_flActualHealthRemoved = 0x68  # unknown_t
    m_iNumHits = 0x6C  # unknown_t
    m_iLastBulletUpdate = 0x70  # unknown_t
    m_bIsOtherEnemy = 0x74  # unknown_t
    m_killType = 0x75  # unknown_t
    pass

class CDestructiblePartsComponent:
    __m_pChainEntity = 0x0  # unknown_t
    m_vecDamageTakenByHitGroup = 0x48  # unknown_t
    m_hOwner = 0x60  # unknown_t
    m_nLastHitDamageLevel = 0x64  # unknown_t
    pass

class CEconItemAttribute:
    m_iAttributeDefinitionIndex = 0x30  # unknown_t
    m_flValue = 0x34  # unknown_t
    m_flInitialValue = 0x38  # unknown_t
    m_nRefundableCurrency = 0x3C  # unknown_t
    m_bSetBonus = 0x40  # unknown_t
    pass

class CEffectData:
    m_vOrigin = 0x8  # unknown_t
    m_vStart = 0x14  # unknown_t
    m_vNormal = 0x20  # unknown_t
    m_vAngles = 0x2C  # unknown_t
    m_hEntity = 0x38  # unknown_t
    m_hOtherEntity = 0x3C  # unknown_t
    m_flScale = 0x40  # unknown_t
    m_flMagnitude = 0x44  # unknown_t
    m_flRadius = 0x48  # unknown_t
    m_nSurfaceProp = 0x4C  # unknown_t
    m_nEffectIndex = 0x50  # unknown_t
    m_nDamageType = 0x58  # unknown_t
    m_nPenetrate = 0x5C  # unknown_t
    m_nMaterial = 0x5E  # unknown_t
    m_nHitBox = 0x60  # unknown_t
    m_nColor = 0x62  # unknown_t
    m_fFlags = 0x63  # unknown_t
    m_nAttachmentIndex = 0x64  # unknown_t
    m_nAttachmentName = 0x68  # string_t
    m_iEffectName = 0x6C  # string_t
    m_nExplosionType = 0x6E  # unknown_t
    pass

class CEntityComponent:
    pass

class CEntityIdentity:
    m_nameStringableIndex = 0x14  # unknown_t
    m_name = 0x18  # unknown_t
    m_designerName = 0x20  # string_t
    m_flags = 0x30  # unknown_t
    m_worldGroupId = 0x38  # unknown_t
    m_fDataObjectTypes = 0x3C  # unknown_t
    m_PathIndex = 0x40  # unknown_t
    m_pPrev = 0x58  # unknown_t
    m_pNext = 0x60  # unknown_t
    m_pPrevByClass = 0x68  # unknown_t
    m_pNextByClass = 0x70  # unknown_t
    pass

class CEntityInstance:
    m_iszPrivateVScripts = 0x8  # unknown_t
    m_pEntity = 0x10  # unknown_t
    m_CScriptComponent = 0x30  # unknown_t
    pass

class CEnvSoundscape:
    m_OnPlay = 0x5F8  # unknown_t
    m_flRadius = 0x620  # unknown_t
    m_soundEventName = 0x628  # string_t
    m_bOverrideWithEvent = 0x630  # unknown_t
    m_soundscapeIndex = 0x634  # unknown_t
    m_soundscapeEntityListId = 0x638  # unknown_t
    m_positionNames = 0x640  # string_t
    m_hProxySoundscape = 0x680  # unknown_t
    m_bDisabled = 0x684  # unknown_t
    m_soundscapeName = 0x688  # string_t
    m_soundEventHash = 0x690  # unknown_t
    pass

class CEnvSoundscapeAlias_snd_soundscape:
    pass

class CEnvSoundscapeProxy:
    m_MainSoundscapeName = 0x698  # string_t
    pass

class CEnvSoundscapeProxyAlias_snd_soundscape_proxy:
    pass

class CEnvSoundscapeTriggerable:
    pass

class CEnvSoundscapeTriggerableAlias_snd_soundscape_triggerable:
    pass

class CFilterAttributeInt:
    m_sAttributeName = 0x650  # string_t
    pass

class CFilterClass:
    m_iFilterClass = 0x650  # unknown_t
    pass

class CFilterLOS:
    pass

class CFilterMassGreater:
    m_fFilterMass = 0x650  # unknown_t
    pass

class CFilterModel:
    m_iFilterModel = 0x650  # unknown_t
    pass

class CFilterMultiple:
    m_nFilterType = 0x650  # unknown_t
    m_iFilterName = 0x658  # string_t
    m_hFilter = 0x6A8  # unknown_t
    pass

class CFilterMultipleAPI:
    pass

class CFilterName:
    m_iFilterName = 0x650  # string_t
    pass

class CFilterProximity:
    m_flRadius = 0x650  # unknown_t
    pass

class CFilterTeam:
    m_iFilterTeam = 0x650  # unknown_t
    pass

class CFuncWater:
    m_BuoyancyHelper = 0xEC8  # unknown_t
    pass

class CGameSceneNode:
    m_bBoneMergeFlex = 0x0  # unknown_t
    m_bDirtyBoneMergeBoneToRoot = 0x0  # unknown_t
    m_bDirtyBoneMergeInfo = 0x0  # unknown_t
    m_bDirtyHierarchy = 0x0  # unknown_t
    m_bNetworkedAnglesChanged = 0x0  # unknown_t
    m_bNetworkedPositionChanged = 0x0  # unknown_t
    m_bNetworkedScaleChanged = 0x0  # unknown_t
    m_bWillBeCallingPostDataUpdate = 0x0  # unknown_t
    m_nLatchAbsOrigin = 0x0  # unknown_t
    m_nodeToWorld = 0x10  # unknown_t
    m_pOwner = 0x30  # unknown_t
    m_pParent = 0x38  # unknown_t
    m_pChild = 0x40  # unknown_t
    m_pNextSibling = 0x48  # unknown_t
    m_hParent = 0x78  # unknown_t
    m_vecOrigin = 0x88  # unknown_t
    m_angRotation = 0xC0  # unknown_t
    m_flScale = 0xCC  # unknown_t
    m_vecAbsOrigin = 0xD0  # unknown_t
    m_angAbsRotation = 0xDC  # unknown_t
    m_flAbsScale = 0xE8  # unknown_t
    m_vecWrappedLocalOrigin = 0xEC  # unknown_t
    m_angWrappedLocalRotation = 0xF8  # unknown_t
    m_flWrappedScale = 0x104  # unknown_t
    m_nParentAttachmentOrBone = 0x108  # unknown_t
    m_bDebugAbsOriginChanges = 0x10A  # unknown_t
    m_bDormant = 0x10B  # unknown_t
    m_bForceParentToBeNetworked = 0x10C  # unknown_t
    m_nHierarchicalDepth = 0x10F  # unknown_t
    m_nHierarchyType = 0x110  # unknown_t
    m_nDoNotSetAnimTimeInInvalidatePhysicsCount = 0x111  # unknown_t
    m_name = 0x114  # unknown_t
    m_hierarchyAttachName = 0x158  # string_t
    m_flZOffset = 0x15C  # unknown_t
    m_flClientLocalScale = 0x160  # unknown_t
    m_vRenderOrigin = 0x164  # unknown_t
    pass

class CGameSceneNodeHandle:
    m_hOwner = 0x8  # unknown_t
    m_name = 0xC  # unknown_t
    pass

class CGlowProperty:
    m_fGlowColor = 0x8  # unknown_t
    m_iGlowType = 0x30  # unknown_t
    m_iGlowTeam = 0x34  # unknown_t
    m_nGlowRange = 0x38  # unknown_t
    m_nGlowRangeMin = 0x3C  # unknown_t
    m_glowColorOverride = 0x40  # unknown_t
    m_bFlashing = 0x44  # unknown_t
    m_flGlowTime = 0x48  # unknown_t
    m_flGlowStartTime = 0x4C  # unknown_t
    m_bEligibleForScreenHighlight = 0x50  # unknown_t
    m_bGlowing = 0x51  # unknown_t
    pass

class CGrenadeTracer:
    m_flTracerDuration = 0xEE0  # unknown_t
    m_nType = 0xEE4  # unknown_t
    pass

class CHitboxComponent:
    m_flBoundsExpandRadius = 0x20  # unknown_t
    pass

class CHostageRescueZone:
    pass

class CHostageRescueZoneShim:
    pass

class CInfoDynamicShadowHint:
    m_bDisabled = 0x5F8  # unknown_t
    m_flRange = 0x5FC  # unknown_t
    m_nImportance = 0x600  # unknown_t
    m_nLightChoice = 0x604  # unknown_t
    m_hLight = 0x608  # unknown_t
    pass

class CInfoDynamicShadowHintBox:
    m_vBoxMins = 0x610  # unknown_t
    m_vBoxMaxs = 0x61C  # unknown_t
    pass

class CInfoFan:
    m_fFanForceMaxRadius = 0x638  # unknown_t
    m_fFanForceMinRadius = 0x63C  # unknown_t
    m_flCurveDistRange = 0x640  # unknown_t
    m_FanForceCurveString = 0x648  # unknown_t
    pass

class CInfoOffscreenPanoramaTexture:
    m_bDisabled = 0x5F8  # unknown_t
    m_nResolutionX = 0x5FC  # unknown_t
    m_nResolutionY = 0x600  # unknown_t
    m_szLayoutFileName = 0x608  # string_t
    m_RenderAttrName = 0x610  # string_t
    m_TargetEntities = 0x618  # CHandle<C_BaseModelEntity>
    m_nTargetChangeCount = 0x630  # unknown_t
    m_vecCSSClasses = 0x638  # unknown_t
    m_bCheckCSSClasses = 0x7B8  # unknown_t
    pass

class CInfoParticleTarget:
    pass

class CInfoTarget:
    pass

class CInfoWorldLayer:
    m_pOutputOnEntitiesSpawned = 0x5F8  # CHandle<C_BaseModelEntity>
    m_worldName = 0x620  # string_t
    m_layerName = 0x628  # string_t
    m_bWorldLayerVisible = 0x630  # unknown_t
    m_bEntitiesSpawned = 0x631  # CHandle<C_BaseModelEntity>
    m_bCreateAsChildSpawnGroup = 0x632  # unknown_t
    m_hLayerSpawnGroup = 0x634  # unknown_t
    m_bWorldLayerActuallyVisible = 0x638  # unknown_t
    pass

class CLightComponent:
    __m_pChainEntity = 0x30  # unknown_t
    m_Color = 0x6D  # unknown_t
    m_SecondaryColor = 0x71  # unknown_t
    m_flBrightness = 0x78  # unknown_t
    m_flBrightnessScale = 0x7C  # unknown_t
    m_flBrightnessMult = 0x80  # unknown_t
    m_flRange = 0x84  # unknown_t
    m_flFalloff = 0x88  # unknown_t
    m_flAttenuation0 = 0x8C  # unknown_t
    m_flAttenuation1 = 0x90  # unknown_t
    m_flAttenuation2 = 0x94  # unknown_t
    m_flTheta = 0x98  # unknown_t
    m_flPhi = 0x9C  # unknown_t
    m_hLightCookie = 0xA0  # unknown_t
    m_nCascades = 0xA8  # unknown_t
    m_nCastShadows = 0xAC  # unknown_t
    m_nShadowWidth = 0xB0  # unknown_t
    m_nShadowHeight = 0xB4  # unknown_t
    m_bRenderDiffuse = 0xB8  # unknown_t
    m_nRenderSpecular = 0xBC  # unknown_t
    m_bRenderTransmissive = 0xC0  # unknown_t
    m_flOrthoLightWidth = 0xC4  # unknown_t
    m_flOrthoLightHeight = 0xC8  # unknown_t
    m_nStyle = 0xCC  # unknown_t
    m_Pattern = 0xD0  # unknown_t
    m_nCascadeRenderStaticObjects = 0xD8  # unknown_t
    m_flShadowCascadeCrossFade = 0xDC  # unknown_t
    m_flShadowCascadeDistanceFade = 0xE0  # unknown_t
    m_flShadowCascadeDistance0 = 0xE4  # unknown_t
    m_flShadowCascadeDistance1 = 0xE8  # unknown_t
    m_flShadowCascadeDistance2 = 0xEC  # unknown_t
    m_flShadowCascadeDistance3 = 0xF0  # unknown_t
    m_nShadowCascadeResolution0 = 0xF4  # unknown_t
    m_nShadowCascadeResolution1 = 0xF8  # unknown_t
    m_nShadowCascadeResolution2 = 0xFC  # unknown_t
    m_nShadowCascadeResolution3 = 0x100  # unknown_t
    m_bUsesBakedShadowing = 0x104  # unknown_t
    m_nShadowPriority = 0x108  # unknown_t
    m_nBakedShadowIndex = 0x10C  # unknown_t
    m_nLightPathUniqueId = 0x110  # unknown_t
    m_nLightMapUniqueId = 0x114  # unknown_t
    m_bRenderToCubemaps = 0x118  # unknown_t
    m_bAllowSSTGeneration = 0x119  # unknown_t
    m_nDirectLight = 0x11C  # unknown_t
    m_nIndirectLight = 0x120  # unknown_t
    m_flFadeMinDist = 0x124  # unknown_t
    m_flFadeMaxDist = 0x128  # unknown_t
    m_flShadowFadeMinDist = 0x12C  # unknown_t
    m_flShadowFadeMaxDist = 0x130  # unknown_t
    m_bEnabled = 0x134  # unknown_t
    m_bFlicker = 0x135  # unknown_t
    m_bPrecomputedFieldsValid = 0x136  # unknown_t
    m_vPrecomputedBoundsMins = 0x138  # unknown_t
    m_vPrecomputedBoundsMaxs = 0x144  # unknown_t
    m_vPrecomputedOBBOrigin = 0x150  # unknown_t
    m_vPrecomputedOBBAngles = 0x15C  # unknown_t
    m_vPrecomputedOBBExtent = 0x168  # unknown_t
    m_flPrecomputedMaxRange = 0x174  # unknown_t
    m_nFogLightingMode = 0x178  # unknown_t
    m_flFogContributionStength = 0x17C  # unknown_t
    m_flNearClipPlane = 0x180  # unknown_t
    m_SkyColor = 0x184  # unknown_t
    m_flSkyIntensity = 0x188  # unknown_t
    m_SkyAmbientBounce = 0x18C  # unknown_t
    m_bUseSecondaryColor = 0x190  # unknown_t
    m_bMixedShadows = 0x191  # unknown_t
    m_flLightStyleStartTime = 0x194  # unknown_t
    m_flCapsuleLength = 0x198  # unknown_t
    m_flMinRoughness = 0x19C  # unknown_t
    pass

class CLogicRelay:
    m_bDisabled = 0x5F8  # unknown_t
    m_bWaitForRefire = 0x5F9  # unknown_t
    m_bTriggerOnce = 0x5FA  # unknown_t
    m_bFastRetrigger = 0x5FB  # unknown_t
    m_bPassthoughCaller = 0x5FC  # unknown_t
    pass

class CLogicRelayAPI:
    pass

class CLogicalEntity:
    pass

class CMapInfo:
    m_iBuyingStatus = 0x5F8  # unknown_t
    m_flBombRadius = 0x5FC  # unknown_t
    m_iPetPopulation = 0x600  # unknown_t
    m_bUseNormalSpawnsForDM = 0x604  # unknown_t
    m_bDisableAutoGeneratedDMSpawns = 0x605  # unknown_t
    m_flBotMaxVisionDistance = 0x608  # unknown_t
    m_iHostageCount = 0x60C  # unknown_t
    m_bFadePlayerVisibilityFarZ = 0x610  # unknown_t
    m_bRainTraceToSkyEnabled = 0x611  # unknown_t
    m_flEnvRainStrength = 0x614  # unknown_t
    m_flEnvPuddleRippleStrength = 0x618  # unknown_t
    m_flEnvPuddleRippleDirection = 0x61C  # unknown_t
    m_flEnvWetnessCoverage = 0x620  # unknown_t
    m_flEnvWetnessDryingAmount = 0x624  # unknown_t
    pass

class CModelState:
    m_hModel = 0xD0  # unknown_t
    m_ModelName = 0xD8  # string_t
    m_bClientClothCreationSuppressed = 0x1A9  # unknown_t
    m_MeshGroupMask = 0x250  # unknown_t
    m_nBodyGroupChoices = 0x2A0  # unknown_t
    m_nIdealMotionType = 0x2EA  # unknown_t
    m_nForceLOD = 0x2EB  # unknown_t
    m_nClothUpdateFlags = 0x2EC  # unknown_t
    pass

class CNetworkedSequenceOperation:
    m_hSequence = 0x8  # unknown_t
    m_flPrevCycle = 0xC  # unknown_t
    m_flCycle = 0x10  # unknown_t
    m_flWeight = 0x14  # unknown_t
    m_bSequenceChangeNetworked = 0x1C  # unknown_t
    m_bDiscontinuity = 0x1D  # unknown_t
    m_flPrevCycleFromDiscontinuity = 0x20  # unknown_t
    m_flPrevCycleForAnimEventDetection = 0x24  # unknown_t
    pass

class CPathQueryComponent:
    pass

class CPathSimple:
    m_CPathQueryComponent = 0x600  # unknown_t
    m_pathString = 0x6F0  # unknown_t
    m_bClosedLoop = 0x6F8  # unknown_t
    pass

class CPathSimpleAPI:
    pass

class CPlayer_AutoaimServices:
    pass

class CPlayer_CameraServices:
    m_vecCsViewPunchAngle = 0x40  # unknown_t
    m_nCsViewPunchAngleTick = 0x4C  # unknown_t
    m_flCsViewPunchAngleTickRatio = 0x50  # unknown_t
    m_PlayerFog = 0x58  # unknown_t
    m_hColorCorrectionCtrl = 0x98  # unknown_t
    m_hViewEntity = 0x9C  # unknown_t
    m_hTonemapController = 0xA0  # unknown_t
    m_audio = 0xA8  # unknown_t
    m_PostProcessingVolumes = 0x120  # unknown_t
    m_flOldPlayerZ = 0x138  # unknown_t
    m_flOldPlayerViewOffsetZ = 0x13C  # unknown_t
    m_CurrentFog = 0x140  # unknown_t
    m_hOldFogController = 0x1A8  # unknown_t
    m_bOverrideFogColor = 0x1AC  # unknown_t
    m_OverrideFogColor = 0x1B1  # unknown_t
    m_bOverrideFogStartEnd = 0x1C5  # unknown_t
    m_fOverrideFogStart = 0x1CC  # unknown_t
    m_fOverrideFogEnd = 0x1E0  # unknown_t
    m_hActivePostProcessingVolume = 0x1F4  # unknown_t
    m_angDemoViewAngles = 0x1F8  # unknown_t
    pass

class CPlayer_FlashlightServices:
    pass

class CPlayer_ItemServices:
    pass

class CPlayer_MovementServices:
    m_nImpulse = 0x40  # unknown_t
    m_nButtons = 0x48  # unknown_t
    m_nQueuedButtonDownMask = 0x68  # unknown_t
    m_nQueuedButtonChangeMask = 0x70  # unknown_t
    m_nButtonDoublePressed = 0x78  # unknown_t
    m_pButtonPressedCmdNumber = 0x80  # unknown_t
    m_nLastCommandNumberProcessed = 0x180  # unknown_t
    m_nToggleButtonDownMask = 0x188  # unknown_t
    m_flMaxspeed = 0x198  # unknown_t
    m_arrForceSubtickMoveWhen = 0x19C  # unknown_t
    m_flForwardMove = 0x1AC  # unknown_t
    m_flLeftMove = 0x1B0  # unknown_t
    m_flUpMove = 0x1B4  # unknown_t
    m_vecLastMovementImpulses = 0x1B8  # unknown_t
    m_vecOldViewAngles = 0x220  # unknown_t
    pass

class CPlayer_MovementServices_Humanoid:
    m_flStepSoundTime = 0x238  # unknown_t
    m_flFallVelocity = 0x23C  # unknown_t
    m_bInCrouch = 0x240  # unknown_t
    m_nCrouchState = 0x244  # unknown_t
    m_flCrouchTransitionStartTime = 0x248  # unknown_t
    m_bDucked = 0x24C  # unknown_t
    m_bDucking = 0x24D  # unknown_t
    m_bInDuckJump = 0x24E  # unknown_t
    m_groundNormal = 0x250  # unknown_t
    m_flSurfaceFriction = 0x25C  # unknown_t
    m_surfaceProps = 0x260  # unknown_t
    m_nStepside = 0x270  # unknown_t
    pass

class CPlayer_ObserverServices:
    m_iObserverMode = 0x40  # unknown_t
    m_hObserverTarget = 0x44  # unknown_t
    m_iObserverLastMode = 0x48  # unknown_t
    m_bForcedObserverMode = 0x4C  # unknown_t
    m_flObserverChaseDistance = 0x50  # unknown_t
    m_flObserverChaseDistanceCalcTime = 0x54  # unknown_t
    pass

class CPlayer_UseServices:
    pass

class CPlayer_WaterServices:
    pass

class CPlayer_WeaponServices:
    m_hMyWeapons = 0x40  # unknown_t
    m_hActiveWeapon = 0x58  # unknown_t
    m_hLastWeapon = 0x5C  # unknown_t
    m_iAmmo = 0x60  # unknown_t
    pass

class CPointChildModifier:
    m_bOrphanInsteadOfDeletingChildrenOnRemove = 0x5F8  # unknown_t
    pass

class CPointOffScreenIndicatorUi:
    m_bBeenEnabled = 0x1130  # unknown_t
    m_bHide = 0x1131  # unknown_t
    m_flSeenTargetTime = 0x1134  # unknown_t
    m_pTargetPanel = 0x1138  # unknown_t
    pass

class CPointOrient:
    m_iszSpawnTargetName = 0x5F8  # string_t
    m_hTarget = 0x600  # unknown_t
    m_bActive = 0x604  # unknown_t
    m_nGoalDirection = 0x608  # unknown_t
    m_nConstraint = 0x60C  # unknown_t
    m_flMaxTurnRate = 0x610  # unknown_t
    m_flLastGameTime = 0x614  # unknown_t
    pass

class CPointTemplate:
    m_iszWorldName = 0x5F8  # string_t
    m_iszSource2EntityLumpName = 0x600  # string_t
    m_iszEntityFilterName = 0x608  # string_t
    m_flTimeoutInterval = 0x610  # unknown_t
    m_bAsynchronouslySpawnEntities = 0x614  # CHandle<C_BaseModelEntity>
    m_clientOnlyEntityBehavior = 0x618  # unknown_t
    m_ownerSpawnGroupType = 0x61C  # unknown_t
    m_createdSpawnGroupHandles = 0x620  # ModelConfigHandle_t
    m_SpawnedEntityHandles = 0x638  # ModelConfigHandle_t
    m_ScriptSpawnCallback = 0x650  # unknown_t
    m_ScriptCallbackScope = 0x658  # unknown_t
    pass

class CPointTemplateAPI:
    pass

class CPrecipitationVData:
    m_szParticlePrecipitationEffect = 0x28  # unknown_t
    m_flInnerDistance = 0x108  # unknown_t
    m_nAttachType = 0x10C  # unknown_t
    m_bBatchSameVolumeType = 0x110  # unknown_t
    m_nRTEnvCP = 0x114  # unknown_t
    m_nRTEnvCPComponent = 0x118  # unknown_t
    m_szModifier = 0x120  # unknown_t
    pass

class CPropDataComponent:
    m_flDmgModBullet = 0x10  # unknown_t
    m_flDmgModClub = 0x14  # unknown_t
    m_flDmgModExplosive = 0x18  # unknown_t
    m_flDmgModFire = 0x1C  # unknown_t
    m_iszPhysicsDamageTableName = 0x20  # string_t
    m_iszBasePropData = 0x28  # unknown_t
    m_nInteractions = 0x30  # unknown_t
    m_bSpawnMotionDisabled = 0x34  # unknown_t
    m_nDisableTakePhysicsDamageSpawnFlag = 0x38  # unknown_t
    m_nMotionDisabledSpawnFlag = 0x3C  # unknown_t
    pass

class CPulseAnimFuncs:
    pass

class CPulseArraylib:
    pass

class CPulseCell_Base:
    m_nEditorNodeID = 0x8  # unknown_t
    pass

class CPulseCell_BaseFlow:
    pass

class CPulseCell_BaseLerp:
    m_WakeResume = 0x48  # unknown_t
    pass

class CPulseCell_BaseLerp__CursorState_t:
    m_StartTime = 0x0  # unknown_t
    m_EndTime = 0x4  # unknown_t
    pass

class CPulseCell_BaseRequirement:
    pass

class CPulseCell_BaseState:
    pass

class CPulseCell_BaseValue:
    pass

class CPulseCell_BaseYieldingInflow:
    pass

class CPulseCell_BooleanSwitchState:
    m_Condition = 0x48  # unknown_t
    m_SubGraph = 0xC0  # unknown_t
    m_WhenTrue = 0x108  # unknown_t
    m_WhenFalse = 0x150  # unknown_t
    pass

class CPulseCell_CursorQueue:
    m_nCursorsAllowedToRunParallel = 0x98  # unknown_t
    pass

class CPulseCell_FireCursors:
    m_Outflows = 0x48  # unknown_t
    m_bWaitForChildOutflows = 0x60  # unknown_t
    m_OnFinished = 0x68  # unknown_t
    m_OnCanceled = 0xB0  # unknown_t
    pass

class CPulseCell_Inflow_BaseEntrypoint:
    m_EntryChunk = 0x48  # unknown_t
    m_RegisterMap = 0x50  # unknown_t
    pass

class CPulseCell_Inflow_EntOutputHandler:
    m_SourceEntity = 0x80  # unknown_t
    m_SourceOutput = 0x90  # unknown_t
    m_ExpectedParamType = 0xA0  # unknown_t
    pass

class CPulseCell_Inflow_EventHandler:
    m_EventName = 0x80  # string_t
    pass

class CPulseCell_Inflow_GraphHook:
    m_HookName = 0x80  # string_t
    pass

class CPulseCell_Inflow_Method:
    m_MethodName = 0x80  # string_t
    m_Description = 0x90  # unknown_t
    m_bIsPublic = 0x98  # unknown_t
    m_ReturnType = 0xA0  # unknown_t
    m_Args = 0xB8  # unknown_t
    pass

class CPulseCell_Inflow_ObservableVariableListener:
    m_nBlackboardReference = 0x80  # unknown_t
    m_bSelfReference = 0x82  # unknown_t
    pass

class CPulseCell_Inflow_Wait:
    m_WakeResume = 0x48  # unknown_t
    pass

class CPulseCell_Inflow_Yield:
    m_UnyieldResume = 0x48  # unknown_t
    pass

class CPulseCell_InlineNodeSkipSelector:
    m_nFlowNodeID = 0x48  # unknown_t
    m_bAnd = 0x4C  # unknown_t
    m_PassOutflow = 0x50  # unknown_t
    m_FailOutflow = 0x68  # unknown_t
    pass

class CPulseCell_IntervalTimer:
    m_Completed = 0x48  # unknown_t
    m_OnInterval = 0x90  # unknown_t
    pass

class CPulseCell_IntervalTimer__CursorState_t:
    m_StartTime = 0x0  # unknown_t
    m_EndTime = 0x4  # unknown_t
    m_flWaitInterval = 0x8  # unknown_t
    m_flWaitIntervalHigh = 0xC  # unknown_t
    m_bCompleteOnNextWake = 0x10  # unknown_t
    pass

class CPulseCell_IsRequirementValid:
    pass

class CPulseCell_IsRequirementValid__Criteria_t:
    m_bIsValid = 0x0  # unknown_t
    pass

class CPulseCell_LerpCameraSettings:
    m_flSeconds = 0x90  # unknown_t
    m_Start = 0x94  # unknown_t
    m_End = 0xA4  # unknown_t
    pass

class CPulseCell_LerpCameraSettings__CursorState_t:
    m_hCamera = 0x8  # unknown_t
    m_OverlaidStart = 0xC  # unknown_t
    m_OverlaidEnd = 0x1C  # unknown_t
    pass

class CPulseCell_LimitCount:
    m_nLimitCount = 0x48  # unknown_t
    pass

class CPulseCell_LimitCount__Criteria_t:
    m_bLimitCountPasses = 0x0  # unknown_t
    pass

class CPulseCell_LimitCount__InstanceState_t:
    m_nCurrentCount = 0x0  # unknown_t
    pass

class CPulseCell_Outflow_CycleOrdered:
    m_Outputs = 0x48  # unknown_t
    pass

class CPulseCell_Outflow_CycleOrdered__InstanceState_t:
    m_nNextIndex = 0x0  # unknown_t
    pass

class CPulseCell_Outflow_CycleRandom:
    m_Outputs = 0x48  # unknown_t
    pass

class CPulseCell_Outflow_CycleShuffled:
    m_Outputs = 0x48  # unknown_t
    pass

class CPulseCell_Outflow_CycleShuffled__InstanceState_t:
    m_Shuffle = 0x0  # unknown_t
    m_nNextShuffle = 0x20  # unknown_t
    pass

class CPulseCell_PickBestOutflowSelector:
    m_nCheckType = 0x48  # unknown_t
    m_OutflowList = 0x50  # unknown_t
    pass

class CPulseCell_PlaySequence:
    m_SequenceName = 0x48  # string_t
    m_PulseAnimEvents = 0x50  # unknown_t
    m_OnFinished = 0x68  # unknown_t
    m_OnCanceled = 0xB0  # unknown_t
    pass

class CPulseCell_PlaySequence__CursorState_t:
    m_hTarget = 0x0  # unknown_t
    pass

class CPulseCell_Step_CallExternalMethod:
    m_MethodName = 0x48  # string_t
    m_GameBlackboard = 0x58  # unknown_t
    m_ExpectedArgs = 0x68  # unknown_t
    m_nAsyncCallMode = 0x78  # unknown_t
    m_OnFinished = 0x80  # unknown_t
    pass

class CPulseCell_Step_DebugLog:
    pass

class CPulseCell_Step_EntFire:
    m_Input = 0x48  # unknown_t
    pass

class CPulseCell_Step_PublicOutput:
    m_OutputIndex = 0x48  # unknown_t
    pass

class CPulseCell_Timeline:
    m_TimelineEvents = 0x48  # unknown_t
    m_bWaitForChildOutflows = 0x60  # unknown_t
    m_OnFinished = 0x68  # unknown_t
    m_OnCanceled = 0xB0  # unknown_t
    pass

class CPulseCell_Timeline__TimelineEvent_t:
    m_flTimeFromPrevious = 0x0  # unknown_t
    m_EventOutflow = 0x8  # unknown_t
    pass

class CPulseCell_Unknown:
    m_UnknownKeys = 0x48  # unknown_t
    pass

class CPulseCell_Value_Curve:
    m_Curve = 0x48  # unknown_t
    pass

class CPulseCell_Value_Gradient:
    m_Gradient = 0x48  # unknown_t
    pass

class CPulseCell_Value_RandomFloat:
    pass

class CPulseCell_Value_RandomInt:
    pass

class CPulseCell_WaitForCursorsWithTag:
    m_bTagSelfWhenComplete = 0x98  # unknown_t
    m_nDesiredKillPriority = 0x9C  # unknown_t
    pass

class CPulseCell_WaitForCursorsWithTagBase:
    m_nCursorsAllowedToWait = 0x48  # unknown_t
    m_WaitComplete = 0x50  # unknown_t
    pass

class CPulseCell_WaitForCursorsWithTagBase__CursorState_t:
    m_TagName = 0x0  # string_t
    pass

class CPulseCell_WaitForObservable:
    m_Condition = 0x48  # unknown_t
    m_OnTrue = 0xC0  # unknown_t
    pass

class CPulseCursorFuncs:
    pass

class CPulseExecCursor:
    pass

class CPulseGameBlackboard:
    m_strGraphName = 0x5F8  # string_t
    m_strStateBlob = 0x600  # unknown_t
    pass

class CPulseGraphDef:
    m_DomainIdentifier = 0x8  # unknown_t
    m_DomainSubType = 0x18  # unknown_t
    m_ParentMapName = 0x30  # string_t
    m_ParentXmlName = 0x40  # string_t
    m_Chunks = 0x50  # unknown_t
    m_Cells = 0x68  # unknown_t
    m_Vars = 0x80  # unknown_t
    m_PublicOutputs = 0x98  # unknown_t
    m_InvokeBindings = 0xB0  # unknown_t
    m_CallInfos = 0xC8  # unknown_t
    m_Constants = 0xE0  # unknown_t
    m_DomainValues = 0xF8  # unknown_t
    m_BlackboardReferences = 0x110  # unknown_t
    m_OutputConnections = 0x128  # unknown_t
    pass

class CPulseMathlib:
    pass

class CPulseTestScriptLib:
    pass

class CPulse_BlackboardReference:
    m_hBlackboardResource = 0x0  # unknown_t
    m_BlackboardResource = 0x8  # unknown_t
    m_nNodeID = 0x18  # unknown_t
    m_NodeName = 0x20  # string_t
    pass

class CPulse_CallInfo:
    m_PortName = 0x0  # string_t
    m_nEditorNodeID = 0x10  # unknown_t
    m_RegisterMap = 0x18  # unknown_t
    m_CallMethodID = 0x48  # unknown_t
    m_nSrcChunk = 0x4C  # unknown_t
    m_nSrcInstruction = 0x50  # unknown_t
    pass

class CPulse_InvokeBinding:
    m_RegisterMap = 0x0  # unknown_t
    m_FuncName = 0x30  # string_t
    m_nCellIndex = 0x40  # unknown_t
    m_nSrcChunk = 0x44  # unknown_t
    m_nSrcInstruction = 0x48  # unknown_t
    pass

class CPulse_OutflowConnection:
    m_SourceOutflowName = 0x0  # string_t
    m_nDestChunk = 0x10  # unknown_t
    m_nInstruction = 0x14  # unknown_t
    m_OutflowRegisterMap = 0x18  # unknown_t
    pass

class CPulse_ResumePoint:
    pass

class CRagdollManager:
    m_iCurrentMaxRagdollCount = 0x5F8  # unknown_t
    pass

class CRenderComponent:
    __m_pChainEntity = 0x10  # unknown_t
    m_bIsRenderingWithViewModels = 0x50  # unknown_t
    m_nSplitscreenFlags = 0x54  # unknown_t
    m_bEnableRendering = 0x58  # unknown_t
    m_bInterpolationReadyToDraw = 0xA8  # unknown_t
    pass

class CSMatchStats_t:
    m_iEnemy5Ks = 0x68  # unknown_t
    m_iEnemy4Ks = 0x6C  # unknown_t
    m_iEnemy3Ks = 0x70  # unknown_t
    m_iEnemyKnifeKills = 0x74  # unknown_t
    m_iEnemyTaserKills = 0x78  # unknown_t
    pass

class CSPerRoundStats_t:
    m_iKills = 0x30  # unknown_t
    m_iDeaths = 0x34  # unknown_t
    m_iAssists = 0x38  # unknown_t
    m_iDamage = 0x3C  # unknown_t
    m_iEquipmentValue = 0x40  # unknown_t
    m_iMoneySaved = 0x44  # unknown_t
    m_iKillReward = 0x48  # unknown_t
    m_iLiveTime = 0x4C  # unknown_t
    m_iHeadShotKills = 0x50  # unknown_t
    m_iObjective = 0x54  # unknown_t
    m_iCashEarned = 0x58  # unknown_t
    m_iUtilityDamage = 0x5C  # unknown_t
    m_iEnemiesFlashed = 0x60  # unknown_t
    pass

class CScriptComponent:
    m_scriptClassName = 0x30  # string_t
    pass

class CServerOnlyModelEntity:
    pass

class CSkeletonInstance:
    m_bDirtyMotionType = 0x0  # unknown_t
    m_bIsGeneratingLatchedParentSpaceState = 0x0  # unknown_t
    m_modelState = 0x190  # unknown_t
    m_bIsAnimationEnabled = 0x490  # unknown_t
    m_bUseParentRenderBounds = 0x491  # unknown_t
    m_bDisableSolidCollisionsForHierarchy = 0x492  # unknown_t
    m_materialGroup = 0x494  # unknown_t
    m_nHitboxSet = 0x498  # unknown_t
    pass

class CSkyboxReference:
    m_worldGroupId = 0x5F8  # unknown_t
    m_hSkyCamera = 0x5FC  # unknown_t
    pass

class CSpriteOriented:
    pass

class CTakeDamageInfoAPI:
    pass

class CTimeline:
    m_flValues = 0x10  # unknown_t
    m_nValueCounts = 0x110  # unknown_t
    m_nBucketCount = 0x210  # unknown_t
    m_flInterval = 0x214  # unknown_t
    m_flFinalValue = 0x218  # unknown_t
    m_nCompressionType = 0x21C  # unknown_t
    m_bStopped = 0x220  # unknown_t
    pass

class CTriggerFan:
    m_vFanOrigin = 0x1008  # unknown_t
    m_vFanOriginOffset = 0x1014  # unknown_t
    m_vFanEnd = 0x1020  # unknown_t
    m_vNoiseDirectionTarget = 0x102C  # unknown_t
    m_vDirection = 0x1038  # unknown_t
    m_bPushTowardsInfoTarget = 0x1044  # unknown_t
    m_bPushAwayFromInfoTarget = 0x1045  # unknown_t
    m_qNoiseDelta = 0x1050  # unknown_t
    m_hInfoFan = 0x1060  # unknown_t
    m_flForce = 0x1064  # unknown_t
    m_bFalloff = 0x1068  # unknown_t
    m_RampTimer = 0x1070  # unknown_t
    pass

class CWaterSplasher:
    pass

class C_AK47:
    pass

class C_AttributeContainer:
    m_Item = 0x50  # unknown_t
    m_iExternalItemProviderRegisteredToken = 0x4C8  # unknown_t
    m_ullRegisteredAsItemID = 0x4D0  # unknown_t
    pass

class C_BarnLight:
    m_bEnabled = 0xEC8  # unknown_t
    m_nColorMode = 0xECC  # unknown_t
    m_Color = 0xED0  # unknown_t
    m_flColorTemperature = 0xED4  # unknown_t
    m_flBrightness = 0xED8  # unknown_t
    m_flBrightnessScale = 0xEDC  # unknown_t
    m_nDirectLight = 0xEE0  # unknown_t
    m_nBakedShadowIndex = 0xEE4  # unknown_t
    m_nLightPathUniqueId = 0xEE8  # unknown_t
    m_nLightMapUniqueId = 0xEEC  # unknown_t
    m_nLuminaireShape = 0xEF0  # unknown_t
    m_flLuminaireSize = 0xEF4  # unknown_t
    m_flLuminaireAnisotropy = 0xEF8  # unknown_t
    m_LightStyleString = 0xF00  # unknown_t
    m_flLightStyleStartTime = 0xF08  # unknown_t
    m_QueuedLightStyleStrings = 0xF10  # unknown_t
    m_LightStyleEvents = 0xF28  # unknown_t
    m_LightStyleTargets = 0xF40  # unknown_t
    m_StyleEvent = 0xF58  # unknown_t
    m_hLightCookie = 0xFF8  # unknown_t
    m_flShape = 0x1000  # unknown_t
    m_flSoftX = 0x1004  # unknown_t
    m_flSoftY = 0x1008  # unknown_t
    m_flSkirt = 0x100C  # unknown_t
    m_flSkirtNear = 0x1010  # unknown_t
    m_vSizeParams = 0x1014  # unknown_t
    m_flRange = 0x1020  # unknown_t
    m_vShear = 0x1024  # unknown_t
    m_nBakeSpecularToCubemaps = 0x1030  # unknown_t
    m_vBakeSpecularToCubemapsSize = 0x1034  # unknown_t
    m_nCastShadows = 0x1040  # unknown_t
    m_nShadowMapSize = 0x1044  # unknown_t
    m_nShadowPriority = 0x1048  # unknown_t
    m_bContactShadow = 0x104C  # unknown_t
    m_bForceShadowsEnabled = 0x104D  # unknown_t
    m_nBounceLight = 0x1050  # unknown_t
    m_flBounceScale = 0x1054  # unknown_t
    m_flMinRoughness = 0x1058  # unknown_t
    m_vAlternateColor = 0x105C  # unknown_t
    m_fAlternateColorBrightness = 0x1068  # unknown_t
    m_nFog = 0x106C  # unknown_t
    m_flFogStrength = 0x1070  # unknown_t
    m_nFogShadows = 0x1074  # unknown_t
    m_flFogScale = 0x1078  # unknown_t
    m_bFogMixedShadows = 0x107C  # unknown_t
    m_flFadeSizeStart = 0x1080  # unknown_t
    m_flFadeSizeEnd = 0x1084  # unknown_t
    m_flShadowFadeSizeStart = 0x1088  # unknown_t
    m_flShadowFadeSizeEnd = 0x108C  # unknown_t
    m_bPrecomputedFieldsValid = 0x1090  # unknown_t
    m_vPrecomputedBoundsMins = 0x1094  # unknown_t
    m_vPrecomputedBoundsMaxs = 0x10A0  # unknown_t
    m_vPrecomputedOBBOrigin = 0x10AC  # unknown_t
    m_vPrecomputedOBBAngles = 0x10B8  # unknown_t
    m_vPrecomputedOBBExtent = 0x10C4  # unknown_t
    m_nPrecomputedSubFrusta = 0x10D0  # unknown_t
    m_vPrecomputedOBBOrigin0 = 0x10D4  # unknown_t
    m_vPrecomputedOBBAngles0 = 0x10E0  # unknown_t
    m_vPrecomputedOBBExtent0 = 0x10EC  # unknown_t
    m_vPrecomputedOBBOrigin1 = 0x10F8  # unknown_t
    m_vPrecomputedOBBAngles1 = 0x1104  # unknown_t
    m_vPrecomputedOBBExtent1 = 0x1110  # unknown_t
    m_vPrecomputedOBBOrigin2 = 0x111C  # unknown_t
    m_vPrecomputedOBBAngles2 = 0x1128  # unknown_t
    m_vPrecomputedOBBExtent2 = 0x1134  # unknown_t
    m_vPrecomputedOBBOrigin3 = 0x1140  # unknown_t
    m_vPrecomputedOBBAngles3 = 0x114C  # unknown_t
    m_vPrecomputedOBBExtent3 = 0x1158  # unknown_t
    m_vPrecomputedOBBOrigin4 = 0x1164  # unknown_t
    m_vPrecomputedOBBAngles4 = 0x1170  # unknown_t
    m_vPrecomputedOBBExtent4 = 0x117C  # unknown_t
    m_vPrecomputedOBBOrigin5 = 0x1188  # unknown_t
    m_vPrecomputedOBBAngles5 = 0x1194  # unknown_t
    m_vPrecomputedOBBExtent5 = 0x11A0  # unknown_t
    m_bInitialBoneSetup = 0x11F0  # unknown_t
    m_VisClusters = 0x11F8  # unknown_t
    pass

class C_BaseButton:
    m_glowEntity = 0xEC8  # unknown_t
    m_usable = 0xECC  # unknown_t
    m_szDisplayText = 0xED0  # unknown_t
    pass

class C_BaseCSGrenade:
    m_bClientPredictDelete = 0x1F90  # unknown_t
    m_bRedraw = 0x1F91  # unknown_t
    m_bIsHeldByPlayer = 0x1F92  # unknown_t
    m_bPinPulled = 0x1F93  # unknown_t
    m_bJumpThrow = 0x1F94  # unknown_t
    m_bThrowAnimating = 0x1F95  # unknown_t
    m_fThrowTime = 0x1F98  # unknown_t
    m_flThrowStrength = 0x1FA0  # unknown_t
    m_fDropTime = 0x2018  # unknown_t
    m_fPinPullTime = 0x201C  # unknown_t
    m_bJustPulledPin = 0x2020  # unknown_t
    m_nNextHoldTick = 0x2024  # unknown_t
    m_flNextHoldFrac = 0x2028  # unknown_t
    m_hSwitchToWeaponAfterThrow = 0x202C  # unknown_t
    pass

class C_BaseCSGrenadeProjectile:
    m_vInitialPosition = 0x13D0  # unknown_t
    m_vInitialVelocity = 0x13DC  # unknown_t
    m_nBounces = 0x13E8  # unknown_t
    m_nExplodeEffectIndex = 0x13F0  # unknown_t
    m_nExplodeEffectTickBegin = 0x13F8  # unknown_t
    m_vecExplodeEffectOrigin = 0x13FC  # unknown_t
    m_flSpawnTime = 0x1408  # unknown_t
    vecLastTrailLinePos = 0x140C  # unknown_t
    flNextTrailLineTime = 0x1418  # unknown_t
    m_bExplodeEffectBegan = 0x141C  # unknown_t
    m_bCanCreateGrenadeTrail = 0x141D  # unknown_t
    m_nSnapshotTrajectoryEffectIndex = 0x1420  # unknown_t
    m_hSnapshotTrajectoryParticleSnapshot = 0x1428  # unknown_t
    m_arrTrajectoryTrailPoints = 0x1430  # unknown_t
    m_arrTrajectoryTrailPointCreationTimes = 0x1448  # unknown_t
    m_flTrajectoryTrailEffectCreationTime = 0x1460  # unknown_t
    pass

class C_BaseClientUIEntity:
    m_bEnabled = 0xED0  # unknown_t
    m_DialogXMLName = 0xED8  # string_t
    m_PanelClassName = 0xEE0  # string_t
    m_PanelID = 0xEE8  # unknown_t
    pass

class C_BaseCombatCharacter:
    m_hMyWearables = 0x1380  # unknown_t
    m_leftFootAttachment = 0x1398  # unknown_t
    m_rightFootAttachment = 0x1399  # unknown_t
    m_nWaterWakeMode = 0x139C  # unknown_t
    m_flWaterWorldZ = 0x13A0  # unknown_t
    m_flWaterNextTraceTime = 0x13A4  # unknown_t
    pass

class C_BaseDoor:
    m_bIsUsable = 0xEC8  # unknown_t
    pass

class C_BaseEntity:
    m_CBodyComponent = 0x38  # unknown_t
    m_NetworkTransmitComponent = 0x40  # unknown_t
    m_nLastThinkTick = 0x328  # unknown_t
    m_pGameSceneNode = 0x330  # unknown_t
    m_pRenderComponent = 0x338  # unknown_t
    m_pCollision = 0x340  # unknown_t
    m_iMaxHealth = 0x348  # unknown_t
    m_iHealth = 0x34C  # unknown_t
    m_lifeState = 0x350  # unknown_t
    m_bTakesDamage = 0x351  # unknown_t
    m_nTakeDamageFlags = 0x358  # unknown_t
    m_nPlatformType = 0x360  # unknown_t
    m_ubInterpolationFrame = 0x361  # unknown_t
    m_hSceneObjectController = 0x364  # unknown_t
    m_nNoInterpolationTick = 0x368  # unknown_t
    m_nVisibilityNoInterpolationTick = 0x36C  # unknown_t
    m_flProxyRandomValue = 0x370  # unknown_t
    m_iEFlags = 0x374  # unknown_t
    m_nWaterType = 0x378  # unknown_t
    m_bInterpolateEvenWithNoModel = 0x379  # unknown_t
    m_bPredictionEligible = 0x37A  # unknown_t
    m_bApplyLayerMatchIDToModel = 0x37B  # unknown_t
    m_tokLayerMatchID = 0x37C  # unknown_t
    m_nSubclassID = 0x380  # unknown_t
    m_nSimulationTick = 0x390  # unknown_t
    m_iCurrentThinkContext = 0x394  # unknown_t
    m_aThinkFunctions = 0x398  # unknown_t
    m_bDisabledContextThinks = 0x3B0  # unknown_t
    m_flAnimTime = 0x3B4  # unknown_t
    m_flSimulationTime = 0x3B8  # unknown_t
    m_nSceneObjectOverrideFlags = 0x3BC  # unknown_t
    m_bHasSuccessfullyInterpolated = 0x3BD  # unknown_t
    m_bHasAddedVarsToInterpolation = 0x3BE  # unknown_t
    m_bRenderEvenWhenNotSuccessfullyInterpolated = 0x3BF  # unknown_t
    m_nInterpolationLatchDirtyFlags = 0x3C0  # unknown_t
    m_ListEntry = 0x3C8  # unknown_t
    m_flCreateTime = 0x3E0  # unknown_t
    m_flSpeed = 0x3E4  # unknown_t
    m_EntClientFlags = 0x3E8  # unknown_t
    m_bClientSideRagdoll = 0x3EA  # unknown_t
    m_iTeamNum = 0x3EB  # unknown_t
    m_spawnflags = 0x3EC  # unknown_t
    m_nNextThinkTick = 0x3F0  # unknown_t
    m_fFlags = 0x3F8  # unknown_t
    m_vecAbsVelocity = 0x3FC  # unknown_t
    m_vecServerVelocity = 0x408  # unknown_t
    m_vecVelocity = 0x430  # unknown_t
    m_vecBaseVelocity = 0x510  # unknown_t
    m_hEffectEntity = 0x51C  # unknown_t
    m_hOwnerEntity = 0x520  # unknown_t
    m_MoveCollide = 0x524  # unknown_t
    m_MoveType = 0x525  # unknown_t
    m_nActualMoveType = 0x526  # unknown_t
    m_flWaterLevel = 0x528  # unknown_t
    m_fEffects = 0x52C  # unknown_t
    m_hGroundEntity = 0x530  # unknown_t
    m_nGroundBodyIndex = 0x534  # unknown_t
    m_flFriction = 0x538  # unknown_t
    m_flElasticity = 0x53C  # unknown_t
    m_flGravityScale = 0x540  # unknown_t
    m_flTimeScale = 0x544  # unknown_t
    m_bAnimatedEveryTick = 0x548  # unknown_t
    m_bGravityDisabled = 0x549  # unknown_t
    m_flNavIgnoreUntilTime = 0x54C  # unknown_t
    m_hThink = 0x550  # unknown_t
    m_fBBoxVisFlags = 0x560  # unknown_t
    m_flActualGravityScale = 0x564  # unknown_t
    m_bGravityActuallyDisabled = 0x568  # unknown_t
    m_bPredictable = 0x569  # unknown_t
    m_bRenderWithViewModels = 0x56A  # unknown_t
    m_nFirstPredictableCommand = 0x56C  # unknown_t
    m_nLastPredictableCommand = 0x570  # unknown_t
    m_hOldMoveParent = 0x574  # unknown_t
    m_Particles = 0x578  # unknown_t
    m_vecAngVelocity = 0x5A8  # unknown_t
    m_DataChangeEventRef = 0x5B4  # unknown_t
    m_dependencies = 0x5B8  # unknown_t
    m_nCreationTick = 0x5D0  # unknown_t
    m_bAnimTimeChanged = 0x5DD  # unknown_t
    m_bSimulationTimeChanged = 0x5DE  # unknown_t
    m_sUniqueHammerID = 0x5E8  # unknown_t
    m_nBloodType = 0x5F0  # unknown_t
    pass

class C_BaseEntityAPI:
    pass

class C_BaseFlex:
    m_flexWeight = 0x1180  # unknown_t
    m_vLookTargetPosition = 0x1198  # unknown_t
    m_blinktoggle = 0x1228  # unknown_t
    m_nLastFlexUpdateFrameCount = 0x1288  # unknown_t
    m_CachedViewTarget = 0x128C  # unknown_t
    m_nNextSceneEventId = 0x1298  # unknown_t
    m_iBlink = 0x129C  # unknown_t
    m_blinktime = 0x12A0  # unknown_t
    m_prevblinktoggle = 0x12A4  # unknown_t
    m_iJawOpen = 0x12A8  # unknown_t
    m_flJawOpenAmount = 0x12AC  # unknown_t
    m_flBlinkAmount = 0x12B0  # unknown_t
    m_iMouthAttachment = 0x12B4  # unknown_t
    m_iEyeAttachment = 0x12B5  # unknown_t
    m_bResetFlexWeightsOnModelChange = 0x12B6  # unknown_t
    m_nEyeOcclusionRendererBone = 0x12D0  # unknown_t
    m_mEyeOcclusionRendererCameraToBoneTransform = 0x12D4  # unknown_t
    m_vEyeOcclusionRendererHalfExtent = 0x1304  # unknown_t
    m_PhonemeClasses = 0x1320  # unknown_t
    pass

class C_BaseFlex__Emphasized_Phoneme:
    m_sClassName = 0x0  # string_t
    m_flAmount = 0x18  # unknown_t
    m_bRequired = 0x1C  # unknown_t
    m_bBasechecked = 0x1D  # unknown_t
    m_bValid = 0x1E  # unknown_t
    pass

class C_BaseGrenade:
    m_bHasWarnedAI = 0x1380  # unknown_t
    m_bIsSmokeGrenade = 0x1381  # unknown_t
    m_bIsLive = 0x1382  # unknown_t
    m_DmgRadius = 0x1384  # unknown_t
    m_flDetonateTime = 0x1388  # unknown_t
    m_flWarnAITime = 0x138C  # unknown_t
    m_flDamage = 0x1390  # unknown_t
    m_iszBounceSound = 0x1398  # unknown_t
    m_ExplosionSound = 0x13A0  # unknown_t
    m_hThrower = 0x13AC  # unknown_t
    m_flNextAttack = 0x13C4  # unknown_t
    m_hOriginalThrower = 0x13C8  # unknown_t
    pass

class C_BaseModelEntity:
    m_CRenderComponent = 0xAE0  # unknown_t
    m_CHitboxComponent = 0xAE8  # unknown_t
    m_pDestructiblePartsSystemComponent = 0xB10  # unknown_t
    m_LastHitGroup = 0xB18  # unknown_t
    m_sLastDamageSourceName = 0xB20  # string_t
    m_vLastDamagePosition = 0xB28  # unknown_t
    m_bInitModelEffects = 0xB50  # unknown_t
    m_bIsStaticProp = 0xB51  # unknown_t
    m_nLastAddDecal = 0xB54  # unknown_t
    m_nDecalsAdded = 0xB58  # unknown_t
    m_iOldHealth = 0xB5C  # unknown_t
    m_nRenderMode = 0xB60  # unknown_t
    m_nRenderFX = 0xB61  # unknown_t
    m_bAllowFadeInView = 0xB62  # unknown_t
    m_clrRender = 0xB80  # unknown_t
    m_vecRenderAttributes = 0xB88  # unknown_t
    m_bRenderToCubemaps = 0xC08  # unknown_t
    m_bNoInterpolate = 0xC09  # unknown_t
    m_Collision = 0xC10  # unknown_t
    m_Glow = 0xCC0  # unknown_t
    m_flGlowBackfaceMult = 0xD18  # unknown_t
    m_fadeMinDist = 0xD1C  # unknown_t
    m_fadeMaxDist = 0xD20  # unknown_t
    m_flFadeScale = 0xD24  # unknown_t
    m_flShadowStrength = 0xD28  # unknown_t
    m_nObjectCulling = 0xD2C  # unknown_t
    m_nAddDecal = 0xD30  # unknown_t
    m_vDecalPosition = 0xD34  # unknown_t
    m_vDecalForwardAxis = 0xD40  # unknown_t
    m_flDecalHealBloodRate = 0xD4C  # unknown_t
    m_flDecalHealHeightRate = 0xD50  # unknown_t
    m_nDecalMode = 0xD54  # unknown_t
    m_nRequiredDecalMode = 0xD55  # unknown_t
    m_ConfigEntitiesToPropagateMaterialDecalsTo = 0xD58  # CHandle<C_BaseModelEntity>
    m_vecViewOffset = 0xD98  # unknown_t
    m_pClientAlphaProperty = 0xE78  # unknown_t
    m_ClientOverrideTint = 0xE80  # unknown_t
    m_bUseClientOverrideTint = 0xE84  # unknown_t
    m_bvDisabledHitGroups = 0xEC0  # unknown_t
    pass

class C_BasePlayerPawn:
    m_pWeaponServices = 0x1408  # unknown_t
    m_pItemServices = 0x1410  # unknown_t
    m_pAutoaimServices = 0x1418  # unknown_t
    m_pObserverServices = 0x1420  # unknown_t
    m_pWaterServices = 0x1428  # unknown_t
    m_pUseServices = 0x1430  # unknown_t
    m_pFlashlightServices = 0x1438  # unknown_t
    m_pCameraServices = 0x1440  # unknown_t
    m_pMovementServices = 0x1448  # unknown_t
    m_ServerViewAngleChanges = 0x1458  # unknown_t
    v_angle = 0x14C0  # unknown_t
    v_anglePrevious = 0x14CC  # unknown_t
    m_iHideHUD = 0x14D8  # unknown_t
    m_skybox3d = 0x14E0  # unknown_t
    m_flDeathTime = 0x1570  # unknown_t
    m_vecPredictionError = 0x1574  # unknown_t
    m_flPredictionErrorTime = 0x1580  # unknown_t
    m_vecLastCameraSetupLocalOrigin = 0x15A0  # unknown_t
    m_flLastCameraSetupTime = 0x15AC  # unknown_t
    m_flFOVSensitivityAdjust = 0x15B0  # unknown_t
    m_flMouseSensitivity = 0x15B4  # unknown_t
    m_vOldOrigin = 0x15B8  # unknown_t
    m_flOldSimulationTime = 0x15C4  # unknown_t
    m_nLastExecutedCommandNumber = 0x15C8  # unknown_t
    m_nLastExecutedCommandTick = 0x15CC  # unknown_t
    m_hController = 0x15D0  # unknown_t
    m_hDefaultController = 0x15D4  # unknown_t
    m_bIsSwappingToPredictableController = 0x15D8  # unknown_t
    pass

class C_BasePlayerWeapon:
    m_nNextPrimaryAttackTick = 0x18F8  # unknown_t
    m_flNextPrimaryAttackTickRatio = 0x18FC  # unknown_t
    m_nNextSecondaryAttackTick = 0x1900  # unknown_t
    m_flNextSecondaryAttackTickRatio = 0x1904  # unknown_t
    m_iClip1 = 0x1908  # unknown_t
    m_iClip2 = 0x190C  # unknown_t
    m_pReserveAmmo = 0x1910  # unknown_t
    pass

class C_BasePropDoor:
    m_eDoorState = 0x1440  # unknown_t
    m_modelChanged = 0x1444  # unknown_t
    m_bLocked = 0x1445  # unknown_t
    m_bNoNPCs = 0x1446  # unknown_t
    m_closedPosition = 0x1448  # unknown_t
    m_closedAngles = 0x1454  # unknown_t
    m_hMaster = 0x1460  # unknown_t
    m_vWhereToSetLightingOrigin = 0x1464  # unknown_t
    pass

class C_BaseToggle:
    pass

class C_BaseTrigger:
    m_OnStartTouch = 0xEC8  # unknown_t
    m_OnStartTouchAll = 0xEF0  # unknown_t
    m_OnEndTouch = 0xF18  # unknown_t
    m_OnEndTouchAll = 0xF40  # unknown_t
    m_OnTouching = 0xF68  # unknown_t
    m_OnTouchingEachEntity = 0xF90  # unknown_t
    m_OnNotTouching = 0xFB8  # unknown_t
    m_hTouchingEntities = 0xFE0  # CHandle<C_BaseModelEntity>
    m_iFilterName = 0xFF8  # string_t
    m_hFilter = 0x1000  # unknown_t
    m_bDisabled = 0x1004  # unknown_t
    pass

class C_Beam:
    m_flFrameRate = 0xEC8  # unknown_t
    m_flHDRColorScale = 0xECC  # unknown_t
    m_flFireTime = 0xED0  # unknown_t
    m_flDamage = 0xED4  # unknown_t
    m_nNumBeamEnts = 0xED8  # unknown_t
    m_queryHandleHalo = 0xEDC  # ModelConfigHandle_t
    m_hBaseMaterial = 0xF00  # unknown_t
    m_nHaloIndex = 0xF08  # unknown_t
    m_nBeamType = 0xF10  # unknown_t
    m_nBeamFlags = 0xF14  # unknown_t
    m_hAttachEntity = 0xF18  # unknown_t
    m_nAttachIndex = 0xF40  # unknown_t
    m_fWidth = 0xF4C  # unknown_t
    m_fEndWidth = 0xF50  # unknown_t
    m_fFadeLength = 0xF54  # unknown_t
    m_fHaloScale = 0xF58  # unknown_t
    m_fAmplitude = 0xF5C  # unknown_t
    m_fStartFrame = 0xF60  # unknown_t
    m_fSpeed = 0xF64  # unknown_t
    m_flFrame = 0xF68  # unknown_t
    m_nClipStyle = 0xF6C  # unknown_t
    m_bTurnedOff = 0xF70  # unknown_t
    m_vecEndPos = 0xF74  # unknown_t
    m_hEndEntity = 0xF80  # unknown_t
    pass

class C_Breakable:
    pass

class C_BreakableProp:
    m_CPropDataComponent = 0x11A0  # unknown_t
    m_OnStartDeath = 0x11E0  # unknown_t
    m_OnBreak = 0x1208  # unknown_t
    m_OnHealthChanged = 0x1230  # unknown_t
    m_OnTakeDamage = 0x1258  # unknown_t
    m_impactEnergyScale = 0x1280  # unknown_t
    m_iMinHealthDmg = 0x1284  # unknown_t
    m_flPressureDelay = 0x1288  # unknown_t
    m_flDefBurstScale = 0x128C  # unknown_t
    m_vDefBurstOffset = 0x1290  # unknown_t
    m_hBreaker = 0x129C  # unknown_t
    m_PerformanceMode = 0x12A0  # unknown_t
    m_flPreventDamageBeforeTime = 0x12A4  # unknown_t
    m_BreakableContentsType = 0x12A8  # unknown_t
    m_strBreakableContentsPropGroupOverride = 0x12B0  # unknown_t
    m_strBreakableContentsParticleOverride = 0x12B8  # unknown_t
    m_bHasBreakPiecesOrCommands = 0x12C0  # unknown_t
    m_explodeDamage = 0x12C4  # unknown_t
    m_explodeRadius = 0x12C8  # unknown_t
    m_explosionDelay = 0x12D0  # unknown_t
    m_explosionBuildupSound = 0x12D8  # unknown_t
    m_explosionCustomEffect = 0x12E0  # unknown_t
    m_explosionCustomSound = 0x12E8  # unknown_t
    m_explosionModifier = 0x12F0  # unknown_t
    m_hPhysicsAttacker = 0x12F8  # unknown_t
    m_flLastPhysicsInfluenceTime = 0x12FC  # unknown_t
    m_flDefaultFadeScale = 0x1300  # unknown_t
    m_hLastAttacker = 0x1304  # unknown_t
    pass

class C_BulletHitModel:
    m_matLocal = 0x1170  # unknown_t
    m_iBoneIndex = 0x11A0  # unknown_t
    m_hPlayerParent = 0x11A4  # unknown_t
    m_bIsHit = 0x11A8  # unknown_t
    m_flTimeCreated = 0x11AC  # unknown_t
    m_vecStartPos = 0x11B0  # unknown_t
    pass

class C_C4:
    m_activeLightParticleIndex = 0x1F90  # unknown_t
    m_eActiveLightEffect = 0x1F94  # unknown_t
    m_bStartedArming = 0x1F98  # unknown_t
    m_fArmedTime = 0x1F9C  # unknown_t
    m_bBombPlacedAnimation = 0x1FA0  # unknown_t
    m_bIsPlantingViaUse = 0x1FA1  # unknown_t
    m_entitySpottedState = 0x1FA8  # unknown_t
    m_nSpotRules = 0x1FC0  # unknown_t
    m_bPlayedArmingBeeps = 0x1FC4  # unknown_t
    m_bBombPlanted = 0x1FCB  # unknown_t
    pass

class C_CS2HudModelAddon:
    pass

class C_CS2HudModelArms:
    pass

class C_CS2HudModelBase:
    pass

class C_CS2HudModelWeapon:
    pass

class C_CS2WeaponModuleBase:
    pass

class C_CSGO_CounterTerroristTeamIntroCamera:
    pass

class C_CSGO_CounterTerroristWingmanIntroCamera:
    pass

class C_CSGO_EndOfMatchCamera:
    pass

class C_CSGO_EndOfMatchCharacterPosition:
    pass

class C_CSGO_EndOfMatchLineupEnd:
    pass

class C_CSGO_EndOfMatchLineupEndpoint:
    pass

class C_CSGO_EndOfMatchLineupStart:
    pass

class C_CSGO_MapPreviewCameraPath:
    m_flZFar = 0x5F8  # unknown_t
    m_flZNear = 0x5FC  # unknown_t
    m_bLoop = 0x600  # unknown_t
    m_bVerticalFOV = 0x601  # unknown_t
    m_bConstantSpeed = 0x602  # unknown_t
    m_flDuration = 0x604  # unknown_t
    m_flPathLength = 0x648  # unknown_t
    m_flPathDuration = 0x64C  # unknown_t
    m_bDofEnabled = 0x664  # unknown_t
    m_flDofNearBlurry = 0x668  # unknown_t
    m_flDofNearCrisp = 0x66C  # unknown_t
    m_flDofFarCrisp = 0x670  # unknown_t
    m_flDofFarBlurry = 0x674  # unknown_t
    m_flDofTiltToGround = 0x678  # unknown_t
    pass

class C_CSGO_MapPreviewCameraPathNode:
    m_szParentPathUniqueID = 0x5F8  # unknown_t
    m_nPathIndex = 0x600  # unknown_t
    m_vInTangentLocal = 0x604  # unknown_t
    m_vOutTangentLocal = 0x610  # unknown_t
    m_flFOV = 0x61C  # unknown_t
    m_flCameraSpeed = 0x620  # unknown_t
    m_flEaseIn = 0x624  # unknown_t
    m_flEaseOut = 0x628  # unknown_t
    m_vInTangentWorld = 0x62C  # unknown_t
    m_vOutTangentWorld = 0x638  # unknown_t
    pass

class C_CSGO_PreviewModel:
    m_animgraph = 0x1380  # unknown_t
    m_animgraphCharacterModeString = 0x1388  # unknown_t
    m_defaultAnim = 0x1390  # unknown_t
    m_nDefaultAnimLoopMode = 0x1398  # unknown_t
    m_flInitialModelScale = 0x139C  # unknown_t
    m_sInitialWeaponState = 0x13A0  # unknown_t
    pass

class C_CSGO_PreviewModelAlias_csgo_item_previewmodel:
    pass

class C_CSGO_PreviewPlayer:
    m_animgraph = 0x3F20  # unknown_t
    m_animgraphCharacterModeString = 0x3F28  # unknown_t
    m_flInitialModelScale = 0x3F30  # unknown_t
    pass

class C_CSGO_PreviewPlayerAlias_csgo_player_previewmodel:
    pass

class C_CSGO_TeamIntroCharacterPosition:
    pass

class C_CSGO_TeamIntroCounterTerroristPosition:
    pass

class C_CSGO_TeamIntroTerroristPosition:
    pass

class C_CSGO_TeamPreviewCamera:
    m_nVariant = 0x680  # unknown_t
    pass

class C_CSGO_TeamPreviewCharacterPosition:
    m_nVariant = 0x5F8  # unknown_t
    m_nRandom = 0x5FC  # unknown_t
    m_nOrdinal = 0x600  # unknown_t
    m_sWeaponName = 0x608  # string_t
    m_xuid = 0x610  # unknown_t
    m_agentItem = 0x618  # unknown_t
    m_glovesItem = 0xA90  # unknown_t
    m_weaponItem = 0xF08  # unknown_t
    pass

class C_CSGO_TeamPreviewModel:
    pass

class C_CSGO_TeamSelectCamera:
    pass

class C_CSGO_TeamSelectCharacterPosition:
    pass

class C_CSGO_TeamSelectCounterTerroristPosition:
    pass

class C_CSGO_TeamSelectTerroristPosition:
    pass

class C_CSGO_TerroristTeamIntroCamera:
    pass

class C_CSGO_TerroristWingmanIntroCamera:
    pass

class C_CSGameRules:
    m_bFreezePeriod = 0x40  # unknown_t
    m_bWarmupPeriod = 0x41  # unknown_t
    m_fWarmupPeriodEnd = 0x44  # unknown_t
    m_fWarmupPeriodStart = 0x48  # unknown_t
    m_bTerroristTimeOutActive = 0x4C  # unknown_t
    m_bCTTimeOutActive = 0x4D  # unknown_t
    m_flTerroristTimeOutRemaining = 0x50  # unknown_t
    m_flCTTimeOutRemaining = 0x54  # unknown_t
    m_nTerroristTimeOuts = 0x58  # unknown_t
    m_nCTTimeOuts = 0x5C  # unknown_t
    m_bTechnicalTimeOut = 0x60  # unknown_t
    m_bMatchWaitingForResume = 0x61  # unknown_t
    m_iRoundTime = 0x64  # unknown_t
    m_fMatchStartTime = 0x68  # unknown_t
    m_fRoundStartTime = 0x6C  # unknown_t
    m_flRestartRoundTime = 0x70  # unknown_t
    m_bGameRestart = 0x74  # unknown_t
    m_flGameStartTime = 0x78  # unknown_t
    m_timeUntilNextPhaseStarts = 0x7C  # unknown_t
    m_gamePhase = 0x80  # unknown_t
    m_totalRoundsPlayed = 0x84  # unknown_t
    m_nRoundsPlayedThisPhase = 0x88  # unknown_t
    m_nOvertimePlaying = 0x8C  # unknown_t
    m_iHostagesRemaining = 0x90  # unknown_t
    m_bAnyHostageReached = 0x94  # unknown_t
    m_bMapHasBombTarget = 0x95  # unknown_t
    m_bMapHasRescueZone = 0x96  # unknown_t
    m_bMapHasBuyZone = 0x97  # unknown_t
    m_bIsQueuedMatchmaking = 0x98  # unknown_t
    m_nQueuedMatchmakingMode = 0x9C  # unknown_t
    m_bIsValveDS = 0xA0  # unknown_t
    m_bLogoMap = 0xA1  # unknown_t
    m_bPlayAllStepSoundsOnServer = 0xA2  # unknown_t
    m_iSpectatorSlotCount = 0xA4  # unknown_t
    m_MatchDevice = 0xA8  # unknown_t
    m_bHasMatchStarted = 0xAC  # unknown_t
    m_nNextMapInMapgroup = 0xB0  # unknown_t
    m_szTournamentEventName = 0xB4  # string_t
    m_szTournamentEventStage = 0x2B4  # unknown_t
    m_szMatchStatTxt = 0x4B4  # unknown_t
    m_szTournamentPredictionsTxt = 0x6B4  # unknown_t
    m_nTournamentPredictionsPct = 0x8B4  # unknown_t
    m_flCMMItemDropRevealStartTime = 0x8B8  # unknown_t
    m_flCMMItemDropRevealEndTime = 0x8BC  # unknown_t
    m_bIsDroppingItems = 0x8C0  # unknown_t
    m_bIsQuestEligible = 0x8C1  # unknown_t
    m_bIsHltvActive = 0x8C2  # unknown_t
    m_arrProhibitedItemIndices = 0x8C4  # unknown_t
    m_arrTournamentActiveCasterAccounts = 0x98C  # unknown_t
    m_numBestOfMaps = 0x99C  # unknown_t
    m_nHalloweenMaskListSeed = 0x9A0  # unknown_t
    m_bBombDropped = 0x9A4  # unknown_t
    m_bBombPlanted = 0x9A5  # unknown_t
    m_iRoundWinStatus = 0x9A8  # unknown_t
    m_eRoundWinReason = 0x9AC  # unknown_t
    m_bTCantBuy = 0x9B0  # unknown_t
    m_bCTCantBuy = 0x9B1  # unknown_t
    m_iMatchStats_RoundResults = 0x9B4  # unknown_t
    m_iMatchStats_PlayersAlive_CT = 0xA2C  # unknown_t
    m_iMatchStats_PlayersAlive_T = 0xAA4  # unknown_t
    m_TeamRespawnWaveTimes = 0xB1C  # unknown_t
    m_flNextRespawnWave = 0xB9C  # unknown_t
    m_vMinimapMins = 0xC1C  # unknown_t
    m_vMinimapMaxs = 0xC28  # unknown_t
    m_MinimapVerticalSectionHeights = 0xC34  # unknown_t
    m_ullLocalMatchID = 0xC58  # unknown_t
    m_nEndMatchMapGroupVoteTypes = 0xC60  # unknown_t
    m_nEndMatchMapGroupVoteOptions = 0xC88  # unknown_t
    m_nEndMatchMapVoteWinner = 0xCB0  # unknown_t
    m_iNumConsecutiveCTLoses = 0xCB4  # unknown_t
    m_iNumConsecutiveTerroristLoses = 0xCB8  # unknown_t
    m_nMatchAbortedEarlyReason = 0xD78  # unknown_t
    m_bHasTriggeredRoundStartMusic = 0xD7C  # unknown_t
    m_bSwitchingTeamsAtRoundReset = 0xD7D  # unknown_t
    m_pGameModeRules = 0xD98  # unknown_t
    m_RetakeRules = 0xDA0  # unknown_t
    m_nMatchEndCount = 0xEB8  # unknown_t
    m_nTTeamIntroVariant = 0xEBC  # unknown_t
    m_nCTTeamIntroVariant = 0xEC0  # unknown_t
    m_bTeamIntroPeriod = 0xEC4  # unknown_t
    m_iRoundEndWinnerTeam = 0xEC8  # unknown_t
    m_eRoundEndReason = 0xECC  # unknown_t
    m_bRoundEndShowTimerDefend = 0xED0  # unknown_t
    m_iRoundEndTimerTime = 0xED4  # unknown_t
    m_sRoundEndFunFactToken = 0xED8  # unknown_t
    m_iRoundEndFunFactPlayerSlot = 0xEE0  # unknown_t
    m_iRoundEndFunFactData1 = 0xEE4  # unknown_t
    m_iRoundEndFunFactData2 = 0xEE8  # unknown_t
    m_iRoundEndFunFactData3 = 0xEEC  # unknown_t
    m_sRoundEndMessage = 0xEF0  # unknown_t
    m_iRoundEndPlayerCount = 0xEF8  # unknown_t
    m_bRoundEndNoMusic = 0xEFC  # unknown_t
    m_iRoundEndLegacy = 0xF00  # unknown_t
    m_nRoundEndCount = 0xF04  # unknown_t
    m_iRoundStartRoundNumber = 0xF08  # unknown_t
    m_nRoundStartCount = 0xF0C  # unknown_t
    m_flLastPerfSampleTime = 0x4F18  # unknown_t
    pass

class C_CSGameRulesProxy:
    m_pGameRules = 0x5F8  # unknown_t
    pass

class C_CSMinimapBoundary:
    pass

class C_CSObserverPawn:
    m_hDetectParentChange = 0x1680  # unknown_t
    pass

class C_CSPetPlacement:
    pass

class C_CSPlayerPawn:
    m_pBulletServices = 0x1690  # unknown_t
    m_pHostageServices = 0x1698  # unknown_t
    m_pBuyServices = 0x16A0  # unknown_t
    m_pGlowServices = 0x16A8  # unknown_t
    m_pActionTrackingServices = 0x16B0  # unknown_t
    m_pDamageReactServices = 0x16B8  # unknown_t
    m_flHealthShotBoostExpirationTime = 0x16C0  # unknown_t
    m_flLastFiredWeaponTime = 0x16C4  # unknown_t
    m_bHasFemaleVoice = 0x16C8  # unknown_t
    m_flLandingTimeSeconds = 0x16CC  # unknown_t
    m_flOldFallVelocity = 0x16D0  # unknown_t
    m_szLastPlaceName = 0x16D4  # string_t
    m_bPrevDefuser = 0x16E6  # unknown_t
    m_bPrevHelmet = 0x16E7  # unknown_t
    m_nPrevArmorVal = 0x16E8  # unknown_t
    m_nPrevGrenadeAmmoCount = 0x16EC  # unknown_t
    m_unPreviousWeaponHash = 0x16F0  # unknown_t
    m_unWeaponHash = 0x16F4  # unknown_t
    m_bInBuyZone = 0x16F8  # unknown_t
    m_bPreviouslyInBuyZone = 0x16F9  # unknown_t
    m_aimPunchAngle = 0x16FC  # unknown_t
    m_aimPunchAngleVel = 0x1708  # unknown_t
    m_aimPunchTickBase = 0x1714  # unknown_t
    m_aimPunchTickFraction = 0x1718  # unknown_t
    m_aimPunchCache = 0x1720  # unknown_t
    m_bInLanding = 0x1740  # unknown_t
    m_flLandingStartTime = 0x1744  # unknown_t
    m_bInHostageRescueZone = 0x1748  # unknown_t
    m_bInBombZone = 0x1749  # unknown_t
    m_bIsBuyMenuOpen = 0x174A  # unknown_t
    m_flTimeOfLastInjury = 0x174C  # unknown_t
    m_flNextSprayDecalTime = 0x1750  # unknown_t
    m_iRetakesOffering = 0x18A8  # unknown_t
    m_iRetakesOfferingCard = 0x18AC  # unknown_t
    m_bRetakesHasDefuseKit = 0x18B0  # unknown_t
    m_bRetakesMVPLastRound = 0x18B1  # unknown_t
    m_iRetakesMVPBoostItem = 0x18B4  # unknown_t
    m_RetakesMVPBoostExtraUtility = 0x18B8  # unknown_t
    m_bNeedToReApplyGloves = 0x18BD  # unknown_t
    m_EconGloves = 0x18C0  # unknown_t
    m_nEconGlovesChanged = 0x1D38  # unknown_t
    m_bMustSyncRagdollState = 0x1D39  # unknown_t
    m_nRagdollDamageBone = 0x1D3C  # unknown_t
    m_vRagdollDamageForce = 0x1D40  # unknown_t
    m_vRagdollDamagePosition = 0x1D4C  # unknown_t
    m_szRagdollDamageWeaponName = 0x1D58  # string_t
    m_bRagdollDamageHeadshot = 0x1D98  # unknown_t
    m_vRagdollServerOrigin = 0x1D9C  # unknown_t
    m_bLastHeadBoneTransformIsValid = 0x2418  # unknown_t
    m_lastLandTime = 0x241C  # unknown_t
    m_bOnGroundLastTick = 0x2420  # unknown_t
    m_hHudModelArms = 0x243C  # unknown_t
    m_qDeathEyeAngles = 0x2440  # unknown_t
    m_bSkipOneHeadConstraintUpdate = 0x244C  # unknown_t
    m_bLeftHanded = 0x244D  # unknown_t
    m_fSwitchedHandednessTime = 0x2450  # unknown_t
    m_flViewmodelOffsetX = 0x2454  # unknown_t
    m_flViewmodelOffsetY = 0x2458  # unknown_t
    m_flViewmodelOffsetZ = 0x245C  # unknown_t
    m_flViewmodelFOV = 0x2460  # unknown_t
    m_vecPlayerPatchEconIndices = 0x2464  # unknown_t
    m_GunGameImmunityColor = 0x2498  # unknown_t
    m_vecBulletHitModels = 0x24E8  # unknown_t
    m_bIsWalking = 0x2500  # unknown_t
    m_thirdPersonHeading = 0x2508  # unknown_t
    m_flSlopeDropOffset = 0x2598  # unknown_t
    m_flSlopeDropHeight = 0x2610  # unknown_t
    m_vHeadConstraintOffset = 0x2688  # unknown_t
    m_entitySpottedState = 0x2718  # unknown_t
    m_bIsScoped = 0x2730  # unknown_t
    m_bResumeZoom = 0x2731  # unknown_t
    m_bIsDefusing = 0x2732  # unknown_t
    m_bIsGrabbingHostage = 0x2733  # unknown_t
    m_iBlockingUseActionInProgress = 0x2734  # unknown_t
    m_flEmitSoundTime = 0x2738  # unknown_t
    m_bInNoDefuseArea = 0x273C  # unknown_t
    m_nWhichBombZone = 0x2740  # unknown_t
    m_iShotsFired = 0x2744  # unknown_t
    m_flFlinchStack = 0x2748  # unknown_t
    m_flVelocityModifier = 0x274C  # unknown_t
    m_flHitHeading = 0x2750  # unknown_t
    m_nHitBodyPart = 0x2754  # unknown_t
    m_bWaitForNoAttack = 0x2758  # unknown_t
    m_ignoreLadderJumpTime = 0x275C  # unknown_t
    m_bKilledByHeadshot = 0x2761  # unknown_t
    m_ArmorValue = 0x2764  # unknown_t
    m_unCurrentEquipmentValue = 0x2768  # unknown_t
    m_unRoundStartEquipmentValue = 0x276A  # unknown_t
    m_unFreezetimeEndEquipmentValue = 0x276C  # unknown_t
    m_nLastKillerIndex = 0x2770  # unknown_t
    m_bOldIsScoped = 0x2774  # unknown_t
    m_bHasDeathInfo = 0x2775  # unknown_t
    m_flDeathInfoTime = 0x2778  # unknown_t
    m_vecDeathInfoOrigin = 0x277C  # unknown_t
    m_grenadeParameterStashTime = 0x278C  # unknown_t
    m_bGrenadeParametersStashed = 0x2790  # unknown_t
    m_angStashedShootAngles = 0x2794  # unknown_t
    m_vecStashedGrenadeThrowPosition = 0x27A0  # unknown_t
    m_vecStashedVelocity = 0x27AC  # unknown_t
    m_angShootAngleHistory = 0x27B8  # unknown_t
    m_vecThrowPositionHistory = 0x27D0  # unknown_t
    m_vecVelocityHistory = 0x27E8  # unknown_t
    m_PredictedDamageTags = 0x2800  # unknown_t
    m_nPrevHighestReceivedDamageTagTick = 0x2868  # unknown_t
    m_nHighestAppliedDamageTagTick = 0x286C  # unknown_t
    m_bShouldAutobuyDMWeapons = 0x3D9C  # unknown_t
    m_fImmuneToGunGameDamageTime = 0x3DA0  # unknown_t
    m_bGunGameImmunity = 0x3DA4  # unknown_t
    m_fImmuneToGunGameDamageTimeLast = 0x3DA8  # unknown_t
    m_fMolotovDamageTime = 0x3DAC  # unknown_t
    m_vecLastAliveLocalVelocity = 0x3DB4  # unknown_t
    m_fRenderingClipPlane = 0x3DC0  # unknown_t
    m_nLastClipPlaneSetupFrame = 0x3DD0  # unknown_t
    m_vecLastClipCameraPos = 0x3DD4  # unknown_t
    m_vecLastClipCameraForward = 0x3DE0  # unknown_t
    m_bClipHitStaticWorld = 0x3DEC  # unknown_t
    m_bCachedPlaneIsValid = 0x3DED  # unknown_t
    m_pClippingWeapon = 0x3DF0  # unknown_t
    m_nPlayerInfernoBodyFx = 0x3DF8  # unknown_t
    m_angEyeAngles = 0x3E00  # unknown_t
    m_arrOldEyeAnglesTimes = 0x3E90  # unknown_t
    m_arrOldEyeAngles = 0x3EA0  # unknown_t
    m_angEyeAnglesVelocity = 0x3ED0  # unknown_t
    m_iIDEntIndex = 0x3EDC  # unknown_t
    m_delayTargetIDTimer = 0x3EE0  # unknown_t
    m_iTargetItemEntIdx = 0x3EF8  # unknown_t
    m_iOldIDEntIndex = 0x3EFC  # unknown_t
    m_holdTargetIDTimer = 0x3F00  # unknown_t
    pass

class C_CSPlayerPawnBase:
    m_pPingServices = 0x15F0  # unknown_t
    m_previousPlayerState = 0x15F8  # unknown_t
    m_iPlayerState = 0x15FC  # unknown_t
    m_bHasMovedSinceSpawn = 0x1600  # unknown_t
    m_flLastSpawnTimeIndex = 0x1604  # unknown_t
    m_iProgressBarDuration = 0x1608  # unknown_t
    m_flProgressBarStartTime = 0x160C  # unknown_t
    m_flClientDeathTime = 0x1610  # unknown_t
    m_flFlashBangTime = 0x1614  # unknown_t
    m_flFlashScreenshotAlpha = 0x1618  # unknown_t
    m_flFlashOverlayAlpha = 0x161C  # unknown_t
    m_bFlashBuildUp = 0x1620  # unknown_t
    m_bFlashDspHasBeenCleared = 0x1621  # unknown_t
    m_bFlashScreenshotHasBeenGrabbed = 0x1622  # unknown_t
    m_flFlashMaxAlpha = 0x1624  # unknown_t
    m_flFlashDuration = 0x1628  # unknown_t
    m_flClientHealthFadeChangeTimestamp = 0x162C  # unknown_t
    m_nClientHealthFadeParityValue = 0x1630  # unknown_t
    m_fNextThinkPushAway = 0x1634  # unknown_t
    m_flCurrentMusicStartTime = 0x163C  # unknown_t
    m_flMusicRoundStartTime = 0x1640  # unknown_t
    m_bDeferStartMusicOnWarmup = 0x1644  # unknown_t
    m_flLastSmokeOverlayAlpha = 0x1648  # unknown_t
    m_flLastSmokeAge = 0x164C  # unknown_t
    m_vLastSmokeOverlayColor = 0x1650  # unknown_t
    m_hOriginalController = 0x1678  # unknown_t
    pass

class C_CSPlayerResource:
    m_bHostageAlive = 0x5F8  # unknown_t
    m_isHostageFollowingSomeone = 0x604  # unknown_t
    m_iHostageEntityIDs = 0x610  # unknown_t
    m_bombsiteCenterA = 0x640  # unknown_t
    m_bombsiteCenterB = 0x64C  # unknown_t
    m_hostageRescueX = 0x658  # unknown_t
    m_hostageRescueY = 0x668  # unknown_t
    m_hostageRescueZ = 0x678  # unknown_t
    m_bEndMatchNextMapAllVoted = 0x688  # unknown_t
    m_foundGoalPositions = 0x689  # unknown_t
    pass

class C_CSTeam:
    m_szTeamMatchStat = 0x6B0  # unknown_t
    m_numMapVictories = 0x8B0  # unknown_t
    m_bSurrendered = 0x8B4  # unknown_t
    m_scoreFirstHalf = 0x8B8  # unknown_t
    m_scoreSecondHalf = 0x8BC  # unknown_t
    m_scoreOvertime = 0x8C0  # unknown_t
    m_szClanTeamname = 0x8C4  # unknown_t
    m_iClanID = 0x948  # unknown_t
    m_szTeamFlagImage = 0x94C  # unknown_t
    m_szTeamLogoImage = 0x954  # unknown_t
    pass

class C_CSWeaponBase:
    m_iWeaponGameplayAnimState = 0x1980  # unknown_t
    m_flWeaponGameplayAnimStateTimestamp = 0x1984  # unknown_t
    m_flInspectCancelCompleteTime = 0x1988  # unknown_t
    m_bInspectPending = 0x198C  # unknown_t
    m_bInspectShouldLoop = 0x198D  # unknown_t
    m_flCrosshairDistance = 0x19B8  # unknown_t
    m_iAmmoLastCheck = 0x19BC  # unknown_t
    m_nLastEmptySoundCmdNum = 0x19C0  # unknown_t
    m_bFireOnEmpty = 0x19C4  # unknown_t
    m_OnPlayerPickup = 0x19C8  # unknown_t
    m_weaponMode = 0x19F0  # unknown_t
    m_flTurningInaccuracyDelta = 0x19F4  # unknown_t
    m_vecTurningInaccuracyEyeDirLast = 0x19F8  # unknown_t
    m_flTurningInaccuracy = 0x1A04  # unknown_t
    m_fAccuracyPenalty = 0x1A08  # unknown_t
    m_flLastAccuracyUpdateTime = 0x1A0C  # unknown_t
    m_fAccuracySmoothedForZoom = 0x1A10  # unknown_t
    m_iRecoilIndex = 0x1A14  # unknown_t
    m_flRecoilIndex = 0x1A18  # unknown_t
    m_bBurstMode = 0x1A1C  # unknown_t
    m_flLastBurstModeChangeTime = 0x1A20  # unknown_t
    m_nPostponeFireReadyTicks = 0x1A24  # unknown_t
    m_flPostponeFireReadyFrac = 0x1A28  # unknown_t
    m_bInReload = 0x1A2C  # unknown_t
    m_flDroppedAtTime = 0x1A30  # unknown_t
    m_bIsHauledBack = 0x1A34  # unknown_t
    m_bSilencerOn = 0x1A35  # unknown_t
    m_flTimeSilencerSwitchComplete = 0x1A38  # unknown_t
    m_iOriginalTeamNumber = 0x1A3C  # unknown_t
    m_iMostRecentTeamNumber = 0x1A40  # unknown_t
    m_bDroppedNearBuyZone = 0x1A44  # unknown_t
    m_flNextAttackRenderTimeOffset = 0x1A48  # unknown_t
    m_bClearWeaponIdentifyingUGC = 0x1AE8  # unknown_t
    m_bVisualsDataSet = 0x1AE9  # unknown_t
    m_bUIWeapon = 0x1AEA  # unknown_t
    m_nCustomEconReloadEventId = 0x1AEC  # unknown_t
    m_nextPrevOwnerUseTime = 0x1AF8  # unknown_t
    m_hPrevOwner = 0x1AFC  # unknown_t
    m_nDropTick = 0x1B00  # unknown_t
    m_bWasActiveWeaponWhenDropped = 0x1B04  # unknown_t
    m_donated = 0x1B24  # unknown_t
    m_fLastShotTime = 0x1B28  # unknown_t
    m_bWasOwnedByCT = 0x1B2C  # unknown_t
    m_bWasOwnedByTerrorist = 0x1B2D  # unknown_t
    m_flNextClientFireBulletTime = 0x1B30  # unknown_t
    m_flNextClientFireBulletTime_Repredict = 0x1B34  # unknown_t
    m_IronSightController = 0x1CA0  # unknown_t
    m_iIronSightMode = 0x1D50  # unknown_t
    m_flLastLOSTraceFailureTime = 0x1D68  # unknown_t
    m_flWatTickOffset = 0x1DC8  # unknown_t
    m_flLastShakeTime = 0x1DDC  # unknown_t
    pass

class C_CSWeaponBaseGun:
    m_zoomLevel = 0x1F90  # unknown_t
    m_iBurstShotsRemaining = 0x1F94  # unknown_t
    m_iSilencerBodygroup = 0x1F98  # unknown_t
    m_silencedModelIndex = 0x1FA8  # unknown_t
    m_inPrecache = 0x1FAC  # unknown_t
    m_bNeedsBoltAction = 0x1FAD  # unknown_t
    m_nRevolverCylinderIdx = 0x1FB0  # unknown_t
    pass

class C_CSWeaponBaseShotgun:
    pass

class C_Chicken:
    m_hHolidayHatAddon = 0x1438  # unknown_t
    m_jumpedThisFrame = 0x143C  # unknown_t
    m_leader = 0x1440  # unknown_t
    m_AttributeManager = 0x1448  # unknown_t
    m_bAttributesInitialized = 0x1920  # unknown_t
    m_hWaterWakeParticles = 0x1924  # unknown_t
    m_bIsPreviewModel = 0x1928  # unknown_t
    pass

class C_ClientRagdoll:
    m_bFadeOut = 0x1170  # unknown_t
    m_bImportant = 0x1171  # unknown_t
    m_flEffectTime = 0x1174  # unknown_t
    m_gibDespawnTime = 0x1178  # unknown_t
    m_iCurrentFriction = 0x117C  # unknown_t
    m_iMinFriction = 0x1180  # unknown_t
    m_iMaxFriction = 0x1184  # unknown_t
    m_iFrictionAnimState = 0x1188  # unknown_t
    m_bReleaseRagdoll = 0x118C  # unknown_t
    m_iEyeAttachment = 0x118D  # unknown_t
    m_bFadingOut = 0x118E  # unknown_t
    m_flScaleEnd = 0x1190  # unknown_t
    m_flScaleTimeStart = 0x11B8  # unknown_t
    m_flScaleTimeEnd = 0x11E0  # unknown_t
    pass

class C_ColorCorrection:
    m_vecOrigin = 0x5F8  # unknown_t
    m_MinFalloff = 0x604  # unknown_t
    m_MaxFalloff = 0x608  # unknown_t
    m_flFadeInDuration = 0x60C  # unknown_t
    m_flFadeOutDuration = 0x610  # unknown_t
    m_flMaxWeight = 0x614  # unknown_t
    m_flCurWeight = 0x618  # unknown_t
    m_netlookupFilename = 0x61C  # unknown_t
    m_bEnabled = 0x81C  # unknown_t
    m_bMaster = 0x81D  # unknown_t
    m_bClientSide = 0x81E  # unknown_t
    m_bExclusive = 0x81F  # unknown_t
    m_bEnabledOnClient = 0x820  # unknown_t
    m_flCurWeightOnClient = 0x824  # unknown_t
    m_bFadingIn = 0x828  # unknown_t
    m_flFadeStartWeight = 0x82C  # unknown_t
    m_flFadeStartTime = 0x830  # unknown_t
    m_flFadeDuration = 0x834  # unknown_t
    pass

class C_ColorCorrectionVolume:
    m_LastEnterWeight = 0x1008  # unknown_t
    m_LastEnterTime = 0x100C  # unknown_t
    m_LastExitWeight = 0x1010  # unknown_t
    m_LastExitTime = 0x1014  # unknown_t
    m_bEnabled = 0x1018  # unknown_t
    m_MaxWeight = 0x101C  # unknown_t
    m_FadeDuration = 0x1020  # unknown_t
    m_Weight = 0x1024  # unknown_t
    m_lookupFilename = 0x1028  # unknown_t
    pass

class C_CsmFovOverride:
    m_cameraName = 0x5F8  # string_t
    m_flCsmFovOverrideValue = 0x600  # unknown_t
    pass

class C_DEagle:
    pass

class C_DecoyGrenade:
    pass

class C_DecoyProjectile:
    m_nDecoyShotTick = 0x1468  # unknown_t
    m_nClientLastKnownDecoyShotTick = 0x146C  # unknown_t
    m_flTimeParticleEffectSpawn = 0x1490  # unknown_t
    pass

class C_DynamicLight:
    m_Flags = 0xEC8  # unknown_t
    m_LightStyle = 0xEC9  # unknown_t
    m_Radius = 0xECC  # unknown_t
    m_Exponent = 0xED0  # unknown_t
    m_InnerAngle = 0xED4  # unknown_t
    m_OuterAngle = 0xED8  # unknown_t
    m_SpotRadius = 0xEDC  # unknown_t
    pass

class C_DynamicProp:
    m_bUseHitboxesForRenderBox = 0x1310  # unknown_t
    m_bUseAnimGraph = 0x1311  # unknown_t
    m_pOutputAnimBegun = 0x1318  # unknown_t
    m_pOutputAnimOver = 0x1340  # unknown_t
    m_pOutputAnimLoopCycleOver = 0x1368  # unknown_t
    m_OnAnimReachedStart = 0x1390  # unknown_t
    m_OnAnimReachedEnd = 0x13B8  # unknown_t
    m_iszIdleAnim = 0x13E0  # unknown_t
    m_nIdleAnimLoopMode = 0x13E8  # unknown_t
    m_bRandomizeCycle = 0x13EC  # unknown_t
    m_bStartDisabled = 0x13ED  # unknown_t
    m_bFiredStartEndOutput = 0x13EE  # unknown_t
    m_bForceNpcExclude = 0x13EF  # unknown_t
    m_bCreateNonSolid = 0x13F0  # unknown_t
    m_bIsOverrideProp = 0x13F1  # unknown_t
    m_iInitialGlowState = 0x13F4  # unknown_t
    m_nGlowRange = 0x13F8  # unknown_t
    m_nGlowRangeMin = 0x13FC  # unknown_t
    m_glowColor = 0x1400  # unknown_t
    m_nGlowTeam = 0x1404  # unknown_t
    m_iCachedFrameCount = 0x1408  # unknown_t
    m_vecCachedRenderMins = 0x140C  # unknown_t
    m_vecCachedRenderMaxs = 0x1418  # unknown_t
    pass

class C_DynamicPropAlias_cable_dynamic:
    pass

class C_DynamicPropAlias_dynamic_prop:
    pass

class C_DynamicPropAlias_prop_dynamic_override:
    pass

class C_EconEntity:
    m_flFlexDelayTime = 0x1390  # unknown_t
    m_flFlexDelayedWeight = 0x1398  # unknown_t
    m_bAttributesInitialized = 0x13A0  # unknown_t
    m_AttributeManager = 0x13A8  # unknown_t
    m_OriginalOwnerXuidLow = 0x1880  # unknown_t
    m_OriginalOwnerXuidHigh = 0x1884  # unknown_t
    m_nFallbackPaintKit = 0x1888  # unknown_t
    m_nFallbackSeed = 0x188C  # unknown_t
    m_flFallbackWear = 0x1890  # unknown_t
    m_nFallbackStatTrak = 0x1894  # unknown_t
    m_bClientside = 0x1898  # unknown_t
    m_bParticleSystemsCreated = 0x1899  # unknown_t
    m_vecAttachedParticles = 0x18A0  # unknown_t
    m_hViewmodelAttachment = 0x18B8  # unknown_t
    m_iOldTeam = 0x18BC  # unknown_t
    m_bAttachmentDirty = 0x18C0  # unknown_t
    m_nUnloadedModelIndex = 0x18C4  # unknown_t
    m_iNumOwnerValidationRetries = 0x18C8  # unknown_t
    m_hOldProvidee = 0x18D8  # unknown_t
    m_vecAttachedModels = 0x18E0  # unknown_t
    pass

class C_EconEntity__AttachedModelData_t:
    m_iModelDisplayFlags = 0x0  # unknown_t
    pass

class C_EconItemView:
    m_bInventoryImageRgbaRequested = 0x60  # unknown_t
    m_bInventoryImageTriedCache = 0x61  # unknown_t
    m_nInventoryImageRgbaWidth = 0x80  # unknown_t
    m_nInventoryImageRgbaHeight = 0x84  # unknown_t
    m_szCurrentLoadCachedFileName = 0x88  # string_t
    m_bRestoreCustomMaterialAfterPrecache = 0x1B8  # unknown_t
    m_iItemDefinitionIndex = 0x1BA  # unknown_t
    m_iEntityQuality = 0x1BC  # unknown_t
    m_iEntityLevel = 0x1C0  # unknown_t
    m_iItemID = 0x1C8  # unknown_t
    m_iItemIDHigh = 0x1D0  # unknown_t
    m_iItemIDLow = 0x1D4  # unknown_t
    m_iAccountID = 0x1D8  # unknown_t
    m_iInventoryPosition = 0x1DC  # unknown_t
    m_bInitialized = 0x1E8  # unknown_t
    m_bDisallowSOC = 0x1E9  # unknown_t
    m_bIsStoreItem = 0x1EA  # unknown_t
    m_bIsTradeItem = 0x1EB  # unknown_t
    m_iEntityQuantity = 0x1EC  # unknown_t
    m_iRarityOverride = 0x1F0  # unknown_t
    m_iQualityOverride = 0x1F4  # unknown_t
    m_iOriginOverride = 0x1F8  # unknown_t
    m_ubStyleOverride = 0x1FC  # unknown_t
    m_unClientFlags = 0x1FD  # unknown_t
    m_AttributeList = 0x210  # unknown_t
    m_NetworkedDynamicAttributes = 0x288  # unknown_t
    m_szCustomName = 0x300  # string_t
    m_szCustomNameOverride = 0x3A1  # string_t
    m_bInitializedTags = 0x470  # unknown_t
    pass

class C_EconWearable:
    m_nForceSkin = 0x18F8  # unknown_t
    m_bAlwaysAllow = 0x18FC  # unknown_t
    pass

class C_EntityDissolve:
    m_flStartTime = 0xED0  # unknown_t
    m_flFadeInStart = 0xED4  # unknown_t
    m_flFadeInLength = 0xED8  # unknown_t
    m_flFadeOutModelStart = 0xEDC  # unknown_t
    m_flFadeOutModelLength = 0xEE0  # unknown_t
    m_flFadeOutStart = 0xEE4  # unknown_t
    m_flFadeOutLength = 0xEE8  # unknown_t
    m_flNextSparkTime = 0xEEC  # unknown_t
    m_nDissolveType = 0xEF0  # unknown_t
    m_vDissolverOrigin = 0xEF4  # unknown_t
    m_nMagnitude = 0xF00  # unknown_t
    m_bCoreExplode = 0xF04  # unknown_t
    m_bLinkedToServerEnt = 0xF05  # unknown_t
    pass

class C_EntityFlame:
    m_hEntAttached = 0x5F8  # unknown_t
    m_hOldAttached = 0x620  # unknown_t
    m_bCheapEffect = 0x624  # unknown_t
    pass

class C_EnvCombinedLightProbeVolume:
    m_Entity_Color = 0x1670  # unknown_t
    m_Entity_flBrightness = 0x1674  # unknown_t
    m_Entity_hCubemapTexture = 0x1678  # unknown_t
    m_Entity_bCustomCubemapTexture = 0x1680  # unknown_t
    m_Entity_hLightProbeTexture_AmbientCube = 0x1688  # unknown_t
    m_Entity_hLightProbeTexture_SDF = 0x1690  # unknown_t
    m_Entity_hLightProbeTexture_SH2_DC = 0x1698  # unknown_t
    m_Entity_hLightProbeTexture_SH2_R = 0x16A0  # unknown_t
    m_Entity_hLightProbeTexture_SH2_G = 0x16A8  # unknown_t
    m_Entity_hLightProbeTexture_SH2_B = 0x16B0  # unknown_t
    m_Entity_hLightProbeDirectLightIndicesTexture = 0x16B8  # unknown_t
    m_Entity_hLightProbeDirectLightScalarsTexture = 0x16C0  # unknown_t
    m_Entity_hLightProbeDirectLightShadowsTexture = 0x16C8  # unknown_t
    m_Entity_vBoxMins = 0x16D0  # unknown_t
    m_Entity_vBoxMaxs = 0x16DC  # unknown_t
    m_Entity_bMoveable = 0x16E8  # unknown_t
    m_Entity_nHandshake = 0x16EC  # unknown_t
    m_Entity_nEnvCubeMapArrayIndex = 0x16F0  # unknown_t
    m_Entity_nPriority = 0x16F4  # unknown_t
    m_Entity_bStartDisabled = 0x16F8  # unknown_t
    m_Entity_flEdgeFadeDist = 0x16FC  # unknown_t
    m_Entity_vEdgeFadeDists = 0x1700  # unknown_t
    m_Entity_nLightProbeSizeX = 0x170C  # unknown_t
    m_Entity_nLightProbeSizeY = 0x1710  # unknown_t
    m_Entity_nLightProbeSizeZ = 0x1714  # unknown_t
    m_Entity_nLightProbeAtlasX = 0x1718  # unknown_t
    m_Entity_nLightProbeAtlasY = 0x171C  # unknown_t
    m_Entity_nLightProbeAtlasZ = 0x1720  # unknown_t
    m_Entity_bEnabled = 0x1739  # unknown_t
    pass

class C_EnvCombinedLightProbeVolumeAlias_func_combined_light_probe_volume:
    pass

class C_EnvCubemap:
    m_Entity_hCubemapTexture = 0x678  # unknown_t
    m_Entity_bCustomCubemapTexture = 0x680  # unknown_t
    m_Entity_flInfluenceRadius = 0x684  # unknown_t
    m_Entity_vBoxProjectMins = 0x688  # unknown_t
    m_Entity_vBoxProjectMaxs = 0x694  # unknown_t
    m_Entity_bMoveable = 0x6A0  # unknown_t
    m_Entity_nHandshake = 0x6A4  # unknown_t
    m_Entity_nEnvCubeMapArrayIndex = 0x6A8  # unknown_t
    m_Entity_nPriority = 0x6AC  # unknown_t
    m_Entity_flEdgeFadeDist = 0x6B0  # unknown_t
    m_Entity_vEdgeFadeDists = 0x6B4  # unknown_t
    m_Entity_flDiffuseScale = 0x6C0  # unknown_t
    m_Entity_bStartDisabled = 0x6C4  # unknown_t
    m_Entity_bDefaultEnvMap = 0x6C5  # unknown_t
    m_Entity_bDefaultSpecEnvMap = 0x6C6  # unknown_t
    m_Entity_bIndoorCubeMap = 0x6C7  # unknown_t
    m_Entity_bCopyDiffuseFromDefaultCubemap = 0x6C8  # unknown_t
    m_Entity_bEnabled = 0x6D8  # unknown_t
    pass

class C_EnvCubemapBox:
    pass

class C_EnvCubemapFog:
    m_flEndDistance = 0x5F8  # unknown_t
    m_flStartDistance = 0x5FC  # unknown_t
    m_flFogFalloffExponent = 0x600  # unknown_t
    m_bHeightFogEnabled = 0x604  # unknown_t
    m_flFogHeightWidth = 0x608  # unknown_t
    m_flFogHeightEnd = 0x60C  # unknown_t
    m_flFogHeightStart = 0x610  # unknown_t
    m_flFogHeightExponent = 0x614  # unknown_t
    m_flLODBias = 0x618  # unknown_t
    m_bActive = 0x61C  # unknown_t
    m_bStartDisabled = 0x61D  # unknown_t
    m_flFogMaxOpacity = 0x620  # unknown_t
    m_nCubemapSourceType = 0x624  # unknown_t
    m_hSkyMaterial = 0x628  # unknown_t
    m_iszSkyEntity = 0x630  # unknown_t
    m_hFogCubemapTexture = 0x638  # unknown_t
    m_bHasHeightFogEnd = 0x640  # unknown_t
    m_bFirstTime = 0x641  # unknown_t
    pass

class C_EnvDecal:
    m_hDecalMaterial = 0xEC8  # unknown_t
    m_flWidth = 0xED0  # unknown_t
    m_flHeight = 0xED4  # unknown_t
    m_flDepth = 0xED8  # unknown_t
    m_nRenderOrder = 0xEDC  # unknown_t
    m_bProjectOnWorld = 0xEE0  # unknown_t
    m_bProjectOnCharacters = 0xEE1  # unknown_t
    m_bProjectOnWater = 0xEE2  # unknown_t
    m_flDepthSortBias = 0xEE4  # unknown_t
    pass

class C_EnvDetailController:
    m_flFadeStartDist = 0x5F8  # unknown_t
    m_flFadeEndDist = 0x5FC  # unknown_t
    pass

class C_EnvLightProbeVolume:
    m_Entity_hLightProbeTexture_AmbientCube = 0x15F0  # unknown_t
    m_Entity_hLightProbeTexture_SDF = 0x15F8  # unknown_t
    m_Entity_hLightProbeTexture_SH2_DC = 0x1600  # unknown_t
    m_Entity_hLightProbeTexture_SH2_R = 0x1608  # unknown_t
    m_Entity_hLightProbeTexture_SH2_G = 0x1610  # unknown_t
    m_Entity_hLightProbeTexture_SH2_B = 0x1618  # unknown_t
    m_Entity_hLightProbeDirectLightIndicesTexture = 0x1620  # unknown_t
    m_Entity_hLightProbeDirectLightScalarsTexture = 0x1628  # unknown_t
    m_Entity_hLightProbeDirectLightShadowsTexture = 0x1630  # unknown_t
    m_Entity_vBoxMins = 0x1638  # unknown_t
    m_Entity_vBoxMaxs = 0x1644  # unknown_t
    m_Entity_bMoveable = 0x1650  # unknown_t
    m_Entity_nHandshake = 0x1654  # unknown_t
    m_Entity_nPriority = 0x1658  # unknown_t
    m_Entity_bStartDisabled = 0x165C  # unknown_t
    m_Entity_nLightProbeSizeX = 0x1660  # unknown_t
    m_Entity_nLightProbeSizeY = 0x1664  # unknown_t
    m_Entity_nLightProbeSizeZ = 0x1668  # unknown_t
    m_Entity_nLightProbeAtlasX = 0x166C  # unknown_t
    m_Entity_nLightProbeAtlasY = 0x1670  # unknown_t
    m_Entity_nLightProbeAtlasZ = 0x1674  # unknown_t
    m_Entity_bEnabled = 0x1681  # unknown_t
    pass

class C_EnvParticleGlow:
    m_flAlphaScale = 0x1478  # unknown_t
    m_flRadiusScale = 0x147C  # unknown_t
    m_flSelfIllumScale = 0x1480  # unknown_t
    m_ColorTint = 0x1484  # unknown_t
    m_hTextureOverride = 0x1488  # unknown_t
    pass

class C_EnvSky:
    m_hSkyMaterial = 0xEC8  # unknown_t
    m_hSkyMaterialLightingOnly = 0xED0  # unknown_t
    m_bStartDisabled = 0xED8  # unknown_t
    m_vTintColor = 0xED9  # unknown_t
    m_vTintColorLightingOnly = 0xEDD  # unknown_t
    m_flBrightnessScale = 0xEE4  # unknown_t
    m_nFogType = 0xEE8  # unknown_t
    m_flFogMinStart = 0xEEC  # unknown_t
    m_flFogMinEnd = 0xEF0  # unknown_t
    m_flFogMaxStart = 0xEF4  # unknown_t
    m_flFogMaxEnd = 0xEF8  # unknown_t
    m_bEnabled = 0xEFC  # unknown_t
    pass

class C_EnvVolumetricFogController:
    m_flScattering = 0x5F8  # unknown_t
    m_TintColor = 0x5FC  # unknown_t
    m_flAnisotropy = 0x600  # unknown_t
    m_flFadeSpeed = 0x604  # unknown_t
    m_flDrawDistance = 0x608  # unknown_t
    m_flFadeInStart = 0x60C  # unknown_t
    m_flFadeInEnd = 0x610  # unknown_t
    m_flIndirectStrength = 0x614  # unknown_t
    m_nVolumeDepth = 0x618  # unknown_t
    m_fFirstVolumeSliceThickness = 0x61C  # unknown_t
    m_nIndirectTextureDimX = 0x620  # unknown_t
    m_nIndirectTextureDimY = 0x624  # unknown_t
    m_nIndirectTextureDimZ = 0x628  # unknown_t
    m_vBoxMins = 0x62C  # unknown_t
    m_vBoxMaxs = 0x638  # unknown_t
    m_bActive = 0x644  # unknown_t
    m_flStartAnisoTime = 0x648  # unknown_t
    m_flStartScatterTime = 0x64C  # unknown_t
    m_flStartDrawDistanceTime = 0x650  # unknown_t
    m_flStartAnisotropy = 0x654  # unknown_t
    m_flStartScattering = 0x658  # unknown_t
    m_flStartDrawDistance = 0x65C  # unknown_t
    m_flDefaultAnisotropy = 0x660  # unknown_t
    m_flDefaultScattering = 0x664  # unknown_t
    m_flDefaultDrawDistance = 0x668  # unknown_t
    m_bStartDisabled = 0x66C  # unknown_t
    m_bEnableIndirect = 0x66D  # unknown_t
    m_bIsMaster = 0x66E  # unknown_t
    m_hFogIndirectTexture = 0x670  # unknown_t
    m_nForceRefreshCount = 0x678  # unknown_t
    m_fNoiseSpeed = 0x67C  # unknown_t
    m_fNoiseStrength = 0x680  # unknown_t
    m_vNoiseScale = 0x684  # unknown_t
    m_fWindSpeed = 0x690  # unknown_t
    m_vWindDirection = 0x694  # unknown_t
    m_bFirstTime = 0x6A0  # unknown_t
    pass

class C_EnvVolumetricFogVolume:
    m_bActive = 0x5F8  # unknown_t
    m_vBoxMins = 0x5FC  # unknown_t
    m_vBoxMaxs = 0x608  # unknown_t
    m_bStartDisabled = 0x614  # unknown_t
    m_bIndirectUseLPVs = 0x615  # unknown_t
    m_flStrength = 0x618  # unknown_t
    m_nFalloffShape = 0x61C  # unknown_t
    m_flFalloffExponent = 0x620  # unknown_t
    m_flHeightFogDepth = 0x624  # unknown_t
    m_fHeightFogEdgeWidth = 0x628  # unknown_t
    m_fIndirectLightStrength = 0x62C  # unknown_t
    m_fSunLightStrength = 0x630  # unknown_t
    m_fNoiseStrength = 0x634  # unknown_t
    m_TintColor = 0x638  # unknown_t
    m_bOverrideTintColor = 0x63C  # unknown_t
    m_bOverrideIndirectLightStrength = 0x63D  # unknown_t
    m_bOverrideSunLightStrength = 0x63E  # unknown_t
    m_bOverrideNoiseStrength = 0x63F  # unknown_t
    pass

class C_EnvWind:
    m_EnvWindShared = 0x5F8  # unknown_t
    pass

class C_EnvWindClientside:
    m_EnvWindShared = 0x5F8  # unknown_t
    pass

class C_EnvWindController:
    m_EnvWindShared = 0x5F8  # unknown_t
    m_fDirectionVariation = 0x6F0  # unknown_t
    m_fSpeedVariation = 0x6F4  # unknown_t
    m_fTurbulence = 0x6F8  # unknown_t
    m_fVolumeHalfExtentXY = 0x6FC  # unknown_t
    m_fVolumeHalfExtentZ = 0x700  # unknown_t
    m_nVolumeResolutionXY = 0x704  # unknown_t
    m_nVolumeResolutionZ = 0x708  # unknown_t
    m_nClipmapLevels = 0x70C  # unknown_t
    m_bIsMaster = 0x710  # unknown_t
    m_bFirstTime = 0x711  # unknown_t
    pass

class C_EnvWindShared:
    m_flStartTime = 0x8  # unknown_t
    m_iWindSeed = 0xC  # unknown_t
    m_iMinWind = 0x10  # unknown_t
    m_iMaxWind = 0x12  # unknown_t
    m_windRadius = 0x14  # unknown_t
    m_iMinGust = 0x18  # unknown_t
    m_iMaxGust = 0x1A  # unknown_t
    m_flMinGustDelay = 0x1C  # unknown_t
    m_flMaxGustDelay = 0x20  # unknown_t
    m_flGustDuration = 0x24  # unknown_t
    m_iGustDirChange = 0x28  # unknown_t
    m_iInitialWindDir = 0x2A  # unknown_t
    m_flInitialWindSpeed = 0x2C  # unknown_t
    m_location = 0x30  # unknown_t
    m_hEntOwner = 0x3C  # unknown_t
    pass

class C_EnvWindVolume:
    m_bActive = 0x5F8  # unknown_t
    m_vBoxMins = 0x5FC  # unknown_t
    m_vBoxMaxs = 0x608  # unknown_t
    m_bStartDisabled = 0x614  # unknown_t
    m_nShape = 0x618  # unknown_t
    m_fWindSpeedMultiplier = 0x61C  # unknown_t
    m_fWindTurbulenceMultiplier = 0x620  # unknown_t
    m_fWindSpeedVariationMultiplier = 0x624  # unknown_t
    m_fWindDirectionVariationMultiplier = 0x628  # unknown_t
    pass

class C_FireCrackerBlast:
    pass

class C_Fish:
    m_pos = 0x1170  # unknown_t
    m_vel = 0x117C  # unknown_t
    m_angles = 0x1188  # unknown_t
    m_localLifeState = 0x1194  # unknown_t
    m_deathDepth = 0x1198  # unknown_t
    m_deathAngle = 0x119C  # unknown_t
    m_buoyancy = 0x11A0  # unknown_t
    m_wiggleTimer = 0x11A8  # unknown_t
    m_wigglePhase = 0x11C0  # unknown_t
    m_wiggleRate = 0x11C4  # unknown_t
    m_actualPos = 0x11C8  # unknown_t
    m_actualAngles = 0x11D4  # unknown_t
    m_poolOrigin = 0x11E0  # unknown_t
    m_waterLevel = 0x11EC  # unknown_t
    m_gotUpdate = 0x11F0  # unknown_t
    m_x = 0x11F4  # unknown_t
    m_y = 0x11F8  # unknown_t
    m_z = 0x11FC  # unknown_t
    m_angle = 0x1200  # unknown_t
    m_errorHistory = 0x1204  # unknown_t
    m_errorHistoryIndex = 0x1254  # unknown_t
    m_errorHistoryCount = 0x1258  # unknown_t
    m_averageError = 0x125C  # unknown_t
    pass

class C_Flashbang:
    pass

class C_FlashbangProjectile:
    pass

class C_FogController:
    m_fog = 0x5F8  # unknown_t
    m_bUseAngles = 0x660  # unknown_t
    m_iChangedVariables = 0x664  # unknown_t
    pass

class C_FootstepControl:
    m_source = 0x1008  # unknown_t
    m_destination = 0x1010  # unknown_t
    pass

class C_FuncBrush:
    pass

class C_FuncConveyor:
    m_vecMoveDirEntitySpace = 0xED0  # unknown_t
    m_flTargetSpeed = 0xEDC  # unknown_t
    m_nTransitionStartTick = 0xEE0  # unknown_t
    m_nTransitionDurationTicks = 0xEE4  # unknown_t
    m_flTransitionStartSpeed = 0xEE8  # unknown_t
    m_hConveyorModels = 0xEF0  # unknown_t
    m_flCurrentConveyorOffset = 0xF08  # unknown_t
    m_flCurrentConveyorSpeed = 0xF0C  # unknown_t
    pass

class C_FuncElectrifiedVolume:
    m_nAmbientEffect = 0xEC8  # unknown_t
    m_EffectName = 0xED0  # string_t
    m_bState = 0xED8  # unknown_t
    pass

class C_FuncLadder:
    m_vecLadderDir = 0xEC8  # unknown_t
    m_Dismounts = 0xED8  # unknown_t
    m_vecLocalTop = 0xEF0  # unknown_t
    m_vecPlayerMountPositionTop = 0xEFC  # unknown_t
    m_vecPlayerMountPositionBottom = 0xF08  # unknown_t
    m_flAutoRideSpeed = 0xF14  # unknown_t
    m_bDisabled = 0xF18  # unknown_t
    m_bFakeLadder = 0xF19  # unknown_t
    m_bHasSlack = 0xF1A  # unknown_t
    pass

class C_FuncMonitor:
    m_targetCamera = 0xEC8  # unknown_t
    m_nResolutionEnum = 0xED0  # unknown_t
    m_bRenderShadows = 0xED4  # unknown_t
    m_bUseUniqueColorTarget = 0xED5  # unknown_t
    m_brushModelName = 0xED8  # string_t
    m_hTargetCamera = 0xEE0  # unknown_t
    m_bEnabled = 0xEE4  # unknown_t
    m_bDraw3DSkybox = 0xEE5  # unknown_t
    pass

class C_FuncMoveLinear:
    pass

class C_FuncMover:
    pass

class C_FuncRotating:
    pass

class C_FuncTrackTrain:
    m_nLongAxis = 0xEC8  # unknown_t
    m_flRadius = 0xECC  # unknown_t
    m_flLineLength = 0xED0  # unknown_t
    pass

class C_GameRules:
    __m_pChainEntity = 0x8  # unknown_t
    m_nTotalPausedTicks = 0x30  # unknown_t
    m_nPauseStartTick = 0x34  # unknown_t
    m_bGamePaused = 0x38  # unknown_t
    pass

class C_GameRulesProxy:
    pass

class C_GlobalLight:
    m_WindClothForceHandle = 0xAC0  # ModelConfigHandle_t
    pass

class C_GradientFog:
    m_hGradientFogTexture = 0x5F8  # unknown_t
    m_flFogStartDistance = 0x600  # unknown_t
    m_flFogEndDistance = 0x604  # unknown_t
    m_bHeightFogEnabled = 0x608  # unknown_t
    m_flFogStartHeight = 0x60C  # unknown_t
    m_flFogEndHeight = 0x610  # unknown_t
    m_flFarZ = 0x614  # unknown_t
    m_flFogMaxOpacity = 0x618  # unknown_t
    m_flFogFalloffExponent = 0x61C  # unknown_t
    m_flFogVerticalExponent = 0x620  # unknown_t
    m_fogColor = 0x624  # unknown_t
    m_flFogStrength = 0x628  # unknown_t
    m_flFadeTime = 0x62C  # unknown_t
    m_bStartDisabled = 0x630  # unknown_t
    m_bIsEnabled = 0x631  # unknown_t
    m_bGradientFogNeedsTextures = 0x632  # unknown_t
    pass

class C_HEGrenade:
    pass

class C_HEGrenadeProjectile:
    pass

class C_HandleTest:
    m_Handle = 0x5F8  # ModelConfigHandle_t
    m_bSendHandle = 0x5FC  # ModelConfigHandle_t
    pass

class C_Hostage:
    m_entitySpottedState = 0x1408  # unknown_t
    m_leader = 0x1420  # unknown_t
    m_reuseTimer = 0x1428  # unknown_t
    m_vel = 0x1440  # unknown_t
    m_isRescued = 0x144C  # unknown_t
    m_jumpedThisFrame = 0x144D  # unknown_t
    m_nHostageState = 0x1450  # unknown_t
    m_bHandsHaveBeenCut = 0x1454  # unknown_t
    m_hHostageGrabber = 0x1458  # unknown_t
    m_fLastGrabTime = 0x145C  # unknown_t
    m_vecGrabbedPos = 0x1460  # unknown_t
    m_flRescueStartTime = 0x146C  # unknown_t
    m_flGrabSuccessTime = 0x1470  # unknown_t
    m_flDropStartTime = 0x1474  # unknown_t
    m_flDeadOrRescuedTime = 0x1478  # unknown_t
    m_blinkTimer = 0x1480  # unknown_t
    m_lookAt = 0x1498  # unknown_t
    m_lookAroundTimer = 0x14A8  # unknown_t
    m_isInit = 0x14C0  # unknown_t
    m_eyeAttachment = 0x14C1  # unknown_t
    m_chestAttachment = 0x14C2  # unknown_t
    m_pPredictionOwner = 0x14C8  # unknown_t
    m_fNewestAlphaThinkTime = 0x14D0  # unknown_t
    pass

class C_HostageCarriableProp:
    pass

class C_IncendiaryGrenade:
    pass

class C_Inferno:
    m_nfxFireDamageEffect = 0xF08  # unknown_t
    m_hInfernoPointsSnapshot = 0xF10  # unknown_t
    m_hInfernoFillerPointsSnapshot = 0xF18  # unknown_t
    m_hInfernoOutlinePointsSnapshot = 0xF20  # unknown_t
    m_hInfernoClimbingOutlinePointsSnapshot = 0xF28  # unknown_t
    m_hInfernoDecalsSnapshot = 0xF30  # unknown_t
    m_firePositions = 0xF38  # unknown_t
    m_fireParentPositions = 0x1238  # unknown_t
    m_bFireIsBurning = 0x1538  # unknown_t
    m_BurnNormal = 0x1578  # unknown_t
    m_fireCount = 0x1878  # unknown_t
    m_nInfernoType = 0x187C  # unknown_t
    m_nFireLifetime = 0x1880  # unknown_t
    m_bInPostEffectTime = 0x1884  # unknown_t
    m_lastFireCount = 0x1888  # unknown_t
    m_nFireEffectTickBegin = 0x188C  # unknown_t
    m_drawableCount = 0x8490  # unknown_t
    m_blosCheck = 0x8494  # unknown_t
    m_nlosperiod = 0x8498  # unknown_t
    m_maxFireHalfWidth = 0x849C  # unknown_t
    m_maxFireHeight = 0x84A0  # unknown_t
    m_minBounds = 0x84A4  # unknown_t
    m_maxBounds = 0x84B0  # unknown_t
    m_flLastGrassBurnThink = 0x84BC  # unknown_t
    pass

class C_InfoInstructorHintHostageRescueZone:
    pass

class C_InfoLadderDismount:
    pass

class C_InfoVisibilityBox:
    m_nMode = 0x5FC  # unknown_t
    m_vBoxSize = 0x600  # unknown_t
    m_bEnabled = 0x60C  # unknown_t
    pass

class C_Item:
    m_pReticleHintTextName = 0x18F8  # string_t
    pass

class C_ItemDogtags:
    m_OwningPlayer = 0x19F8  # unknown_t
    m_KillingPlayer = 0x19FC  # unknown_t
    pass

class C_Item_Healthshot:
    pass

class C_KeychainModule:
    m_nKeychainDefID = 0x1178  # unknown_t
    m_nKeychainSeed = 0x117C  # unknown_t
    pass

class C_Knife:
    m_bFirstAttack = 0x1F90  # unknown_t
    pass

class C_LateUpdatedAnimating:
    pass

class C_LightDirectionalEntity:
    pass

class C_LightEntity:
    m_CLightComponent = 0xEC8  # unknown_t
    pass

class C_LightEnvironmentEntity:
    pass

class C_LightOrthoEntity:
    pass

class C_LightSpotEntity:
    pass

class C_LocalTempEntity:
    flags = 0x1170  # unknown_t
    die = 0x1174  # unknown_t
    m_flFrameMax = 0x1178  # unknown_t
    x = 0x117C  # unknown_t
    y = 0x1180  # unknown_t
    fadeSpeed = 0x1184  # unknown_t
    bounceFactor = 0x1188  # unknown_t
    hitSound = 0x118C  # unknown_t
    priority = 0x1190  # unknown_t
    tentOffset = 0x1194  # unknown_t
    m_vecTempEntAngVelocity = 0x11A0  # unknown_t
    tempent_renderamt = 0x11AC  # unknown_t
    m_vecNormal = 0x11B0  # unknown_t
    m_flSpriteScale = 0x11BC  # unknown_t
    m_nFlickerFrame = 0x11C0  # unknown_t
    m_flFrameRate = 0x11C4  # unknown_t
    m_flFrame = 0x11C8  # unknown_t
    m_pszImpactEffect = 0x11D0  # unknown_t
    m_pszParticleEffect = 0x11D8  # unknown_t
    m_bParticleCollision = 0x11E0  # unknown_t
    m_iLastCollisionFrame = 0x11E4  # unknown_t
    m_vLastCollisionOrigin = 0x11E8  # unknown_t
    m_vecTempEntVelocity = 0x11F4  # unknown_t
    m_vecPrevAbsOrigin = 0x1200  # unknown_t
    m_vecTempEntAcceleration = 0x120C  # unknown_t
    pass

class C_MapPreviewParticleSystem:
    pass

class C_MapVetoPickController:
    m_nDraftType = 0x608  # unknown_t
    m_nTeamWinningCoinToss = 0x60C  # unknown_t
    m_nTeamWithFirstChoice = 0x610  # unknown_t
    m_nVoteMapIdsList = 0x710  # unknown_t
    m_nAccountIDs = 0x72C  # unknown_t
    m_nMapId0 = 0x82C  # unknown_t
    m_nMapId1 = 0x92C  # unknown_t
    m_nMapId2 = 0xA2C  # unknown_t
    m_nMapId3 = 0xB2C  # unknown_t
    m_nMapId4 = 0xC2C  # unknown_t
    m_nMapId5 = 0xD2C  # unknown_t
    m_nStartingSide0 = 0xE2C  # unknown_t
    m_nCurrentPhase = 0xF2C  # unknown_t
    m_nPhaseStartTick = 0xF30  # unknown_t
    m_nPhaseDurationTicks = 0xF34  # unknown_t
    m_nPostDataUpdateTick = 0xF38  # unknown_t
    m_bDisabledHud = 0xF3C  # unknown_t
    pass

class C_ModelPointEntity:
    pass

class C_MolotovGrenade:
    pass

class C_MolotovProjectile:
    m_bIsIncGrenade = 0x1468  # unknown_t
    pass

class C_Multimeter:
    m_hTargetC4 = 0x1178  # unknown_t
    pass

class C_MultiplayRules:
    pass

class C_NametagModule:
    m_strNametagString = 0x1178  # string_t
    pass

class C_NetTestBaseCombatCharacter:
    pass

class C_OmniLight:
    m_flInnerAngle = 0x1218  # unknown_t
    m_flOuterAngle = 0x121C  # unknown_t
    m_bShowLight = 0x1220  # unknown_t
    pass

class C_ParticleSystem:
    m_szSnapshotFileName = 0xEC8  # string_t
    m_bActive = 0x10C8  # unknown_t
    m_bFrozen = 0x10C9  # unknown_t
    m_flFreezeTransitionDuration = 0x10CC  # unknown_t
    m_nStopType = 0x10D0  # unknown_t
    m_bAnimateDuringGameplayPause = 0x10D4  # unknown_t
    m_iEffectIndex = 0x10D8  # unknown_t
    m_flStartTime = 0x10E0  # unknown_t
    m_flPreSimTime = 0x10E4  # unknown_t
    m_vServerControlPoints = 0x10E8  # unknown_t
    m_iServerControlPointAssignments = 0x1118  # unknown_t
    m_hControlPointEnts = 0x111C  # unknown_t
    m_bNoSave = 0x121C  # unknown_t
    m_bNoFreeze = 0x121D  # unknown_t
    m_bNoRamp = 0x121E  # unknown_t
    m_bStartActive = 0x121F  # unknown_t
    m_iszEffectName = 0x1220  # string_t
    m_iszControlPointNames = 0x1228  # string_t
    m_nDataCP = 0x1428  # unknown_t
    m_vecDataCPValue = 0x142C  # unknown_t
    m_nTintCP = 0x1438  # unknown_t
    m_clrTint = 0x143C  # unknown_t
    m_bOldActive = 0x1460  # unknown_t
    m_bOldFrozen = 0x1461  # unknown_t
    pass

class C_PathParticleRope:
    m_bStartActive = 0x600  # unknown_t
    m_flMaxSimulationTime = 0x604  # unknown_t
    m_iszEffectName = 0x608  # string_t
    m_PathNodes_Name = 0x610  # string_t
    m_flParticleSpacing = 0x628  # unknown_t
    m_flSlack = 0x62C  # unknown_t
    m_flRadius = 0x630  # unknown_t
    m_ColorTint = 0x634  # unknown_t
    m_nEffectState = 0x638  # unknown_t
    m_iEffectIndex = 0x640  # unknown_t
    m_PathNodes_Position = 0x648  # unknown_t
    m_PathNodes_TangentIn = 0x660  # unknown_t
    m_PathNodes_TangentOut = 0x678  # unknown_t
    m_PathNodes_Color = 0x690  # unknown_t
    m_PathNodes_PinEnabled = 0x6A8  # unknown_t
    m_PathNodes_RadiusScale = 0x6C0  # unknown_t
    pass

class C_PathParticleRopeAlias_path_particle_rope_clientside:
    pass

class C_PhysBox:
    pass

class C_PhysMagnet:
    m_aAttachedObjectsFromServer = 0x1170  # unknown_t
    m_aAttachedObjects = 0x1188  # unknown_t
    pass

class C_PhysPropClientside:
    m_flTouchDelta = 0x1310  # unknown_t
    m_fDeathTime = 0x1314  # unknown_t
    m_vecDamagePosition = 0x1318  # unknown_t
    m_vecDamageDirection = 0x1324  # unknown_t
    m_nDamageType = 0x1330  # unknown_t
    pass

class C_PhysicsProp:
    m_bAwake = 0x1310  # unknown_t
    pass

class C_PhysicsPropMultiplayer:
    pass

class C_PlantedC4:
    m_bBombTicking = 0x1178  # unknown_t
    m_nBombSite = 0x117C  # unknown_t
    m_nSourceSoundscapeHash = 0x1180  # unknown_t
    m_entitySpottedState = 0x1188  # unknown_t
    m_flNextGlow = 0x11A0  # unknown_t
    m_flNextBeep = 0x11A4  # unknown_t
    m_flC4Blow = 0x11A8  # unknown_t
    m_bCannotBeDefused = 0x11AC  # unknown_t
    m_bHasExploded = 0x11AD  # unknown_t
    m_flTimerLength = 0x11B0  # unknown_t
    m_bBeingDefused = 0x11B4  # unknown_t
    m_bTriggerWarning = 0x11B8  # unknown_t
    m_bExplodeWarning = 0x11BC  # unknown_t
    m_bC4Activated = 0x11C0  # unknown_t
    m_bTenSecWarning = 0x11C1  # unknown_t
    m_flDefuseLength = 0x11C4  # unknown_t
    m_flDefuseCountDown = 0x11C8  # unknown_t
    m_bBombDefused = 0x11CC  # unknown_t
    m_hBombDefuser = 0x11D0  # unknown_t
    m_AttributeManager = 0x11D8  # unknown_t
    m_hDefuserMultimeter = 0x16B0  # unknown_t
    m_flNextRadarFlashTime = 0x16B4  # unknown_t
    m_bRadarFlash = 0x16B8  # unknown_t
    m_pBombDefuser = 0x16BC  # unknown_t
    m_fLastDefuseTime = 0x16C0  # unknown_t
    m_pPredictionOwner = 0x16C8  # unknown_t
    m_vecC4ExplodeSpectatePos = 0x16D0  # unknown_t
    m_vecC4ExplodeSpectateAng = 0x16DC  # unknown_t
    m_flC4ExplodeSpectateDuration = 0x16E8  # unknown_t
    pass

class C_PlayerPing:
    m_hPlayer = 0x628  # unknown_t
    m_hPingedEntity = 0x62C  # unknown_t
    m_iType = 0x630  # unknown_t
    m_bUrgent = 0x634  # unknown_t
    m_szPlaceName = 0x635  # string_t
    pass

class C_PlayerSprayDecal:
    m_nUniqueID = 0xEC8  # unknown_t
    m_unAccountID = 0xECC  # unknown_t
    m_unTraceID = 0xED0  # unknown_t
    m_rtGcTime = 0xED4  # unknown_t
    m_vecEndPos = 0xED8  # unknown_t
    m_vecStart = 0xEE4  # unknown_t
    m_vecLeft = 0xEF0  # unknown_t
    m_vecNormal = 0xEFC  # unknown_t
    m_nPlayer = 0xF08  # unknown_t
    m_nEntity = 0xF0C  # unknown_t
    m_nHitbox = 0xF10  # unknown_t
    m_flCreationTime = 0xF14  # unknown_t
    m_nTintID = 0xF18  # unknown_t
    m_nVersion = 0xF1C  # unknown_t
    m_ubSignature = 0xF1D  # unknown_t
    m_SprayRenderHelper = 0xFA8  # unknown_t
    pass

class C_PlayerVisibility:
    m_flVisibilityStrength = 0x5F8  # unknown_t
    m_flFogDistanceMultiplier = 0x5FC  # unknown_t
    m_flFogMaxDensityMultiplier = 0x600  # unknown_t
    m_flFadeTime = 0x604  # unknown_t
    m_bStartDisabled = 0x608  # unknown_t
    m_bIsEnabled = 0x609  # unknown_t
    pass

class C_PointCamera:
    m_FOV = 0x5F8  # unknown_t
    m_Resolution = 0x5FC  # unknown_t
    m_bFogEnable = 0x600  # unknown_t
    m_FogColor = 0x601  # unknown_t
    m_flFogStart = 0x608  # unknown_t
    m_flFogEnd = 0x60C  # unknown_t
    m_flFogMaxDensity = 0x610  # unknown_t
    m_bActive = 0x614  # unknown_t
    m_bUseScreenAspectRatio = 0x615  # unknown_t
    m_flAspectRatio = 0x618  # unknown_t
    m_bNoSky = 0x61C  # unknown_t
    m_fBrightness = 0x620  # unknown_t
    m_flZFar = 0x624  # unknown_t
    m_flZNear = 0x628  # unknown_t
    m_bCanHLTVUse = 0x62C  # unknown_t
    m_bAlignWithParent = 0x62D  # unknown_t
    m_bDofEnabled = 0x62E  # unknown_t
    m_flDofNearBlurry = 0x630  # unknown_t
    m_flDofNearCrisp = 0x634  # unknown_t
    m_flDofFarCrisp = 0x638  # unknown_t
    m_flDofFarBlurry = 0x63C  # unknown_t
    m_flDofTiltToGround = 0x640  # unknown_t
    m_TargetFOV = 0x644  # unknown_t
    m_DegreesPerSecond = 0x648  # unknown_t
    m_bIsOn = 0x64C  # unknown_t
    m_pNext = 0x650  # unknown_t
    pass

class C_PointCameraVFOV:
    m_flVerticalFOV = 0x658  # unknown_t
    pass

class C_PointClientUIDialog:
    m_hActivator = 0xEF8  # unknown_t
    m_bStartEnabled = 0xEFC  # unknown_t
    pass

class C_PointClientUIHUD:
    m_bCheckCSSClasses = 0xF00  # unknown_t
    m_bIgnoreInput = 0x1080  # unknown_t
    m_flWidth = 0x1084  # unknown_t
    m_flHeight = 0x1088  # unknown_t
    m_flDPI = 0x108C  # unknown_t
    m_flInteractDistance = 0x1090  # unknown_t
    m_flDepthOffset = 0x1094  # unknown_t
    m_unOwnerContext = 0x1098  # unknown_t
    m_unHorizontalAlign = 0x109C  # unknown_t
    m_unVerticalAlign = 0x10A0  # unknown_t
    m_unOrientation = 0x10A4  # unknown_t
    m_bAllowInteractionFromAllSceneWorlds = 0x10A8  # unknown_t
    m_vecCSSClasses = 0x10B0  # unknown_t
    pass

class C_PointClientUIWorldPanel:
    m_bForceRecreateNextUpdate = 0xF00  # unknown_t
    m_bMoveViewToPlayerNextThink = 0xF01  # unknown_t
    m_bCheckCSSClasses = 0xF02  # unknown_t
    m_anchorDeltaTransform = 0xF10  # unknown_t
    m_pOffScreenIndicator = 0x10A8  # unknown_t
    m_bIgnoreInput = 0x10D0  # unknown_t
    m_bLit = 0x10D1  # unknown_t
    m_bFollowPlayerAcrossTeleport = 0x10D2  # unknown_t
    m_flWidth = 0x10D4  # unknown_t
    m_flHeight = 0x10D8  # unknown_t
    m_flDPI = 0x10DC  # unknown_t
    m_flInteractDistance = 0x10E0  # unknown_t
    m_flDepthOffset = 0x10E4  # unknown_t
    m_unOwnerContext = 0x10E8  # unknown_t
    m_unHorizontalAlign = 0x10EC  # unknown_t
    m_unVerticalAlign = 0x10F0  # unknown_t
    m_unOrientation = 0x10F4  # unknown_t
    m_bAllowInteractionFromAllSceneWorlds = 0x10F8  # unknown_t
    m_vecCSSClasses = 0x1100  # unknown_t
    m_bOpaque = 0x1118  # unknown_t
    m_bNoDepth = 0x1119  # unknown_t
    m_bVisibleWhenParentNoDraw = 0x111A  # unknown_t
    m_bRenderBackface = 0x111B  # unknown_t
    m_bUseOffScreenIndicator = 0x111C  # unknown_t
    m_bExcludeFromSaveGames = 0x111D  # unknown_t
    m_bGrabbable = 0x111E  # unknown_t
    m_bOnlyRenderToTexture = 0x111F  # unknown_t
    m_bDisableMipGen = 0x1120  # unknown_t
    m_nExplicitImageLayout = 0x1124  # unknown_t
    pass

class C_PointClientUIWorldTextPanel:
    m_messageText = 0x1130  # unknown_t
    pass

class C_PointCommentaryNode:
    m_bActive = 0x1188  # unknown_t
    m_bWasActive = 0x1189  # unknown_t
    m_flEndTime = 0x118C  # unknown_t
    m_flStartTime = 0x1190  # unknown_t
    m_flStartTimeInCommentary = 0x1194  # unknown_t
    m_iszCommentaryFile = 0x1198  # unknown_t
    m_iszTitle = 0x11A0  # unknown_t
    m_iszSpeakers = 0x11A8  # unknown_t
    m_iNodeNumber = 0x11B0  # unknown_t
    m_iNodeNumberMax = 0x11B4  # unknown_t
    m_bListenedTo = 0x11B8  # unknown_t
    m_hViewPosition = 0x11C8  # unknown_t
    m_bRestartAfterRestore = 0x11CC  # unknown_t
    pass

class C_PointEntity:
    pass

class C_PointValueRemapper:
    m_bDisabled = 0x5F8  # unknown_t
    m_bDisabledOld = 0x5F9  # unknown_t
    m_bUpdateOnClient = 0x5FA  # unknown_t
    m_nInputType = 0x5FC  # unknown_t
    m_hRemapLineStart = 0x600  # unknown_t
    m_hRemapLineEnd = 0x604  # unknown_t
    m_flMaximumChangePerSecond = 0x608  # unknown_t
    m_flDisengageDistance = 0x60C  # unknown_t
    m_flEngageDistance = 0x610  # unknown_t
    m_bRequiresUseKey = 0x614  # unknown_t
    m_nOutputType = 0x618  # unknown_t
    m_hOutputEntities = 0x620  # CHandle<C_BaseModelEntity>
    m_nHapticsType = 0x638  # unknown_t
    m_nMomentumType = 0x63C  # unknown_t
    m_flMomentumModifier = 0x640  # unknown_t
    m_flSnapValue = 0x644  # unknown_t
    m_flCurrentMomentum = 0x648  # unknown_t
    m_nRatchetType = 0x64C  # unknown_t
    m_flRatchetOffset = 0x650  # unknown_t
    m_flInputOffset = 0x654  # unknown_t
    m_bEngaged = 0x658  # unknown_t
    m_bFirstUpdate = 0x659  # unknown_t
    m_flPreviousValue = 0x65C  # unknown_t
    m_flPreviousUpdateTickTime = 0x660  # unknown_t
    m_vecPreviousTestPoint = 0x664  # unknown_t
    pass

class C_PointWorldText:
    m_bForceRecreateNextUpdate = 0xED0  # unknown_t
    m_messageText = 0xEE8  # unknown_t
    m_FontName = 0x10E8  # string_t
    m_BackgroundMaterialName = 0x1128  # string_t
    m_bEnabled = 0x1168  # unknown_t
    m_bFullbright = 0x1169  # unknown_t
    m_flWorldUnitsPerPx = 0x116C  # unknown_t
    m_flFontSize = 0x1170  # unknown_t
    m_flDepthOffset = 0x1174  # unknown_t
    m_bDrawBackground = 0x1178  # unknown_t
    m_flBackgroundBorderWidth = 0x117C  # unknown_t
    m_flBackgroundBorderHeight = 0x1180  # unknown_t
    m_flBackgroundWorldToUV = 0x1184  # unknown_t
    m_Color = 0x1188  # unknown_t
    m_nJustifyHorizontal = 0x118C  # unknown_t
    m_nJustifyVertical = 0x1190  # unknown_t
    m_nReorientMode = 0x1194  # unknown_t
    pass

class C_PortraitWorldCallbackHandler:
    pass

class C_PostProcessingVolume:
    m_hPostSettings = 0x1018  # unknown_t
    m_flFadeDuration = 0x1020  # unknown_t
    m_flMinLogExposure = 0x1024  # unknown_t
    m_flMaxLogExposure = 0x1028  # unknown_t
    m_flMinExposure = 0x102C  # unknown_t
    m_flMaxExposure = 0x1030  # unknown_t
    m_flExposureCompensation = 0x1034  # unknown_t
    m_flExposureFadeSpeedUp = 0x1038  # unknown_t
    m_flExposureFadeSpeedDown = 0x103C  # unknown_t
    m_flTonemapEVSmoothingRange = 0x1040  # unknown_t
    m_bMaster = 0x1044  # unknown_t
    m_bExposureControl = 0x1045  # unknown_t
    pass

class C_Precipitation:
    m_flDensity = 0x1008  # unknown_t
    m_flParticleInnerDist = 0x1018  # unknown_t
    m_pParticleDef = 0x1020  # unknown_t
    m_tParticlePrecipTraceTimer = 0x1048  # unknown_t
    m_bActiveParticlePrecipEmitter = 0x1050  # unknown_t
    m_bParticlePrecipInitialized = 0x1051  # unknown_t
    m_bHasSimulatedSinceLastSceneObjectUpdate = 0x1052  # unknown_t
    m_nAvailableSheetSequencesMaxIndex = 0x1054  # unknown_t
    pass

class C_PrecipitationBlocker:
    pass

class C_PropDoorRotating:
    pass

class C_RagdollProp:
    m_ragEnabled = 0x1178  # unknown_t
    m_ragPos = 0x1190  # unknown_t
    m_ragAngles = 0x11A8  # unknown_t
    m_flBlendWeight = 0x11C0  # unknown_t
    m_hRagdollSource = 0x11C4  # unknown_t
    m_iEyeAttachment = 0x11C8  # unknown_t
    m_flBlendWeightCurrent = 0x11CC  # unknown_t
    m_parentPhysicsBoneIndices = 0x11D0  # unknown_t
    m_worldSpaceBoneComputationOrder = 0x11E8  # unknown_t
    pass

class C_RagdollPropAttached:
    m_boneIndexAttached = 0x1200  # unknown_t
    m_ragdollAttachedObjectIndex = 0x1204  # unknown_t
    m_attachmentPointBoneSpace = 0x1208  # unknown_t
    m_attachmentPointRagdollSpace = 0x1214  # unknown_t
    m_vecOffset = 0x1220  # unknown_t
    m_parentTime = 0x122C  # unknown_t
    m_bHasParent = 0x1230  # unknown_t
    pass

class C_RectLight:
    m_bShowLight = 0x1218  # unknown_t
    pass

class C_RetakeGameRules:
    m_nMatchSeed = 0xF8  # unknown_t
    m_bBlockersPresent = 0xFC  # unknown_t
    m_bRoundInProgress = 0xFD  # unknown_t
    m_iFirstSecondHalfRound = 0x100  # unknown_t
    m_iBombSite = 0x104  # unknown_t
    pass

class C_RopeKeyframe:
    m_bEndPointAttachmentAnglesDirty = 0x0  # unknown_t
    m_bEndPointAttachmentPositionsDirty = 0x0  # unknown_t
    m_bNewDataThisFrame = 0x0  # unknown_t
    m_bPhysicsInitted = 0x0  # unknown_t
    m_LinksTouchingSomething = 0xED0  # unknown_t
    m_nLinksTouchingSomething = 0xED4  # unknown_t
    m_bApplyWind = 0xED8  # unknown_t
    m_fPrevLockedPoints = 0xEDC  # unknown_t
    m_iForcePointMoveCounter = 0xEE0  # unknown_t
    m_bPrevEndPointPos = 0xEE4  # unknown_t
    m_vPrevEndPointPos = 0xEE8  # unknown_t
    m_flCurScroll = 0xF00  # unknown_t
    m_flScrollSpeed = 0xF04  # unknown_t
    m_RopeFlags = 0xF08  # unknown_t
    m_iRopeMaterialModelIndex = 0xF10  # unknown_t
    m_nSegments = 0x1188  # unknown_t
    m_hStartPoint = 0x118C  # unknown_t
    m_hEndPoint = 0x1190  # unknown_t
    m_iStartAttachment = 0x1194  # unknown_t
    m_iEndAttachment = 0x1195  # unknown_t
    m_Subdiv = 0x1196  # unknown_t
    m_RopeLength = 0x1198  # unknown_t
    m_Slack = 0x119A  # unknown_t
    m_TextureScale = 0x119C  # unknown_t
    m_fLockedPoints = 0x11A0  # unknown_t
    m_nChangeCount = 0x11A1  # unknown_t
    m_Width = 0x11A4  # unknown_t
    m_PhysicsDelegate = 0x11A8  # unknown_t
    m_hMaterial = 0x11B8  # unknown_t
    m_TextureHeight = 0x11C0  # unknown_t
    m_vecImpulse = 0x11C4  # unknown_t
    m_vecPreviousImpulse = 0x11D0  # unknown_t
    m_flCurrentGustTimer = 0x11DC  # unknown_t
    m_flCurrentGustLifetime = 0x11E0  # unknown_t
    m_flTimeToNextGust = 0x11E4  # unknown_t
    m_vWindDir = 0x11E8  # unknown_t
    m_vColorMod = 0x11F4  # unknown_t
    m_vCachedEndPointAttachmentPos = 0x1200  # unknown_t
    m_vCachedEndPointAttachmentAngle = 0x1218  # unknown_t
    m_bConstrainBetweenEndpoints = 0x1230  # unknown_t
    pass

class C_RopeKeyframe__CPhysicsDelegate:
    m_pKeyframe = 0x8  # unknown_t
    pass

class C_SceneEntity:
    m_bIsPlayingBack = 0x600  # unknown_t
    m_bPaused = 0x601  # unknown_t
    m_bMultiplayer = 0x602  # unknown_t
    m_bAutogenerated = 0x603  # unknown_t
    m_flForceClientTime = 0x604  # unknown_t
    m_nSceneStringIndex = 0x608  # unknown_t
    m_bClientOnly = 0x60A  # unknown_t
    m_hOwner = 0x60C  # unknown_t
    m_hActorList = 0x610  # unknown_t
    m_bWasPlaying = 0x628  # unknown_t
    m_QueuedEvents = 0x638  # unknown_t
    m_flCurrentTime = 0x650  # unknown_t
    pass

class C_SceneEntity__QueuedEvents_t:
    starttime = 0x0  # unknown_t
    pass

class C_ShatterGlassShardPhysics:
    m_ShardDesc = 0x1328  # unknown_t
    pass

class C_SingleplayRules:
    pass

class C_SkyCamera:
    m_skyboxData = 0x5F8  # unknown_t
    m_skyboxSlotToken = 0x688  # unknown_t
    m_bUseAngles = 0x68C  # unknown_t
    m_pNext = 0x690  # unknown_t
    pass

class C_SmokeGrenade:
    pass

class C_SmokeGrenadeProjectile:
    m_nSmokeEffectTickBegin = 0x1480  # unknown_t
    m_bDidSmokeEffect = 0x1484  # unknown_t
    m_nRandomSeed = 0x1488  # unknown_t
    m_vSmokeColor = 0x148C  # unknown_t
    m_vSmokeDetonationPos = 0x1498  # unknown_t
    m_VoxelFrameData = 0x14A8  # unknown_t
    m_nVoxelFrameDataSize = 0x14C0  # unknown_t
    m_nVoxelUpdate = 0x14C4  # unknown_t
    m_bSmokeVolumeDataReceived = 0x14C8  # unknown_t
    m_bSmokeEffectSpawned = 0x14C9  # unknown_t
    pass

class C_SoundAreaEntityBase:
    m_bDisabled = 0x5F8  # unknown_t
    m_bWasEnabled = 0x600  # unknown_t
    m_iszSoundAreaType = 0x608  # unknown_t
    m_vPos = 0x610  # unknown_t
    pass

class C_SoundAreaEntityOrientedBox:
    m_vMin = 0x620  # unknown_t
    m_vMax = 0x62C  # unknown_t
    pass

class C_SoundAreaEntitySphere:
    m_flRadius = 0x620  # unknown_t
    pass

class C_SoundEventAABBEntity:
    m_vMins = 0x6C0  # unknown_t
    m_vMaxs = 0x6CC  # unknown_t
    pass

class C_SoundEventEntity:
    m_bClientSideOnly = 0x0  # unknown_t
    m_bStartOnSpawn = 0x5F8  # unknown_t
    m_bToLocalPlayer = 0x5F9  # unknown_t
    m_bStopOnNew = 0x5FA  # unknown_t
    m_bSaveRestore = 0x5FB  # unknown_t
    m_bSavedIsPlaying = 0x5FC  # unknown_t
    m_flSavedElapsedTime = 0x600  # unknown_t
    m_iszSourceEntityName = 0x608  # string_t
    m_iszAttachmentName = 0x610  # string_t
    m_onGUIDChanged = 0x618  # unknown_t
    m_onSoundFinished = 0x640  # unknown_t
    m_flClientCullRadius = 0x668  # unknown_t
    m_iszSoundName = 0x698  # string_t
    m_hSource = 0x6B4  # unknown_t
    m_nEntityIndexSelection = 0x6B8  # unknown_t
    pass

class C_SoundEventEntityAlias_snd_event_point:
    pass

class C_SoundEventOBBEntity:
    m_vMins = 0x6C0  # unknown_t
    m_vMaxs = 0x6CC  # unknown_t
    pass

class C_SoundEventPathCornerEntity:
    m_vecCornerPairsNetworked = 0x6C0  # unknown_t
    pass

class C_SoundEventSphereEntity:
    m_flRadius = 0x6C0  # unknown_t
    pass

class C_SoundOpvarSetAABBEntity:
    pass

class C_SoundOpvarSetAutoRoomEntity:
    pass

class C_SoundOpvarSetOBBEntity:
    pass

class C_SoundOpvarSetOBBWindEntity:
    pass

class C_SoundOpvarSetPathCornerEntity:
    pass

class C_SoundOpvarSetPointBase:
    m_iszStackName = 0x5F8  # string_t
    m_iszOperatorName = 0x600  # string_t
    m_iszOpvarName = 0x608  # string_t
    m_iOpvarIndex = 0x610  # unknown_t
    m_bUseAutoCompare = 0x614  # unknown_t
    pass

class C_SoundOpvarSetPointEntity:
    pass

class C_SpotlightEnd:
    m_flLightScale = 0xEC8  # unknown_t
    m_Radius = 0xECC  # unknown_t
    pass

class C_Sprite:
    m_hSpriteMaterial = 0xEC8  # unknown_t
    m_hAttachedToEntity = 0xED0  # unknown_t
    m_nAttachment = 0xED4  # unknown_t
    m_flSpriteFramerate = 0xED8  # unknown_t
    m_flFrame = 0xEDC  # unknown_t
    m_flDieTime = 0xEE0  # unknown_t
    m_nBrightness = 0xEF0  # unknown_t
    m_flBrightnessDuration = 0xEF4  # unknown_t
    m_flSpriteScale = 0xEF8  # unknown_t
    m_flScaleDuration = 0xEFC  # unknown_t
    m_bWorldSpaceScale = 0xF00  # unknown_t
    m_flGlowProxySize = 0xF04  # unknown_t
    m_flHDRColorScale = 0xF08  # unknown_t
    m_flLastTime = 0xF0C  # unknown_t
    m_flMaxFrame = 0xF10  # unknown_t
    m_flStartScale = 0xF14  # unknown_t
    m_flDestScale = 0xF18  # unknown_t
    m_flScaleTimeStart = 0xF1C  # unknown_t
    m_nStartBrightness = 0xF20  # unknown_t
    m_nDestBrightness = 0xF24  # unknown_t
    m_flBrightnessTimeStart = 0xF28  # unknown_t
    m_nSpriteWidth = 0xF38  # unknown_t
    m_nSpriteHeight = 0xF3C  # unknown_t
    pass

class C_StattrakModule:
    m_bKnife = 0x1178  # unknown_t
    pass

class C_Team:
    m_aPlayerControllers = 0x5F8  # unknown_t
    m_aPlayers = 0x610  # unknown_t
    m_iScore = 0x628  # unknown_t
    m_szTeamname = 0x62C  # unknown_t
    pass

class C_TeamplayRules:
    pass

class C_TextureBasedAnimatable:
    m_bLoop = 0xEC8  # unknown_t
    m_flFPS = 0xECC  # unknown_t
    m_hPositionKeys = 0xED0  # unknown_t
    m_hRotationKeys = 0xED8  # unknown_t
    m_vAnimationBoundsMin = 0xEE0  # unknown_t
    m_vAnimationBoundsMax = 0xEEC  # unknown_t
    m_flStartTime = 0xEF8  # unknown_t
    m_flStartFrame = 0xEFC  # unknown_t
    pass

class C_TintController:
    pass

class C_TonemapController2:
    m_flAutoExposureMin = 0x5F8  # unknown_t
    m_flAutoExposureMax = 0x5FC  # unknown_t
    m_flExposureAdaptationSpeedUp = 0x600  # unknown_t
    m_flExposureAdaptationSpeedDown = 0x604  # unknown_t
    m_flTonemapEVSmoothingRange = 0x608  # unknown_t
    pass

class C_TonemapController2Alias_env_tonemap_controller2:
    pass

class C_TriggerBuoyancy:
    m_BuoyancyHelper = 0x1008  # unknown_t
    m_flFluidDensity = 0x1120  # unknown_t
    pass

class C_TriggerLerpObject:
    pass

class C_TriggerMultiple:
    pass

class C_TriggerPhysics:
    m_gravityScale = 0x1008  # unknown_t
    m_linearLimit = 0x100C  # unknown_t
    m_linearDamping = 0x1010  # unknown_t
    m_angularLimit = 0x1014  # unknown_t
    m_angularDamping = 0x1018  # unknown_t
    m_linearForce = 0x101C  # unknown_t
    m_flFrequency = 0x1020  # unknown_t
    m_flDampingRatio = 0x1024  # unknown_t
    m_vecLinearForcePointAt = 0x1028  # unknown_t
    m_bCollapseToForcePoint = 0x1034  # unknown_t
    m_vecLinearForcePointAtWorld = 0x1038  # unknown_t
    m_vecLinearForceDirection = 0x1044  # unknown_t
    m_bConvertToDebrisWhenPossible = 0x1050  # unknown_t
    pass

class C_TriggerVolume:
    pass

class C_VoteController:
    m_iActiveIssueIndex = 0x608  # unknown_t
    m_iOnlyTeamToVote = 0x60C  # unknown_t
    m_nVoteOptionCount = 0x610  # unknown_t
    m_nPotentialVotes = 0x624  # unknown_t
    m_bVotesDirty = 0x628  # unknown_t
    m_bTypeDirty = 0x629  # unknown_t
    m_bIsYesNoVote = 0x62A  # unknown_t
    pass

class C_WaterBullet:
    pass

class C_WeaponAWP:
    pass

class C_WeaponAug:
    pass

class C_WeaponBaseItem:
    m_bSequenceInProgress = 0x1F90  # unknown_t
    m_bRedraw = 0x1F91  # unknown_t
    pass

class C_WeaponBizon:
    pass

class C_WeaponCZ75a:
    m_bMagazineRemoved = 0x1FC0  # unknown_t
    pass

class C_WeaponElite:
    pass

class C_WeaponFamas:
    pass

class C_WeaponFiveSeven:
    pass

class C_WeaponG3SG1:
    pass

class C_WeaponGalilAR:
    pass

class C_WeaponGlock:
    pass

class C_WeaponHKP2000:
    pass

class C_WeaponM249:
    pass

class C_WeaponM4A1:
    pass

class C_WeaponM4A1Silencer:
    pass

class C_WeaponMAC10:
    pass

class C_WeaponMP5SD:
    pass

class C_WeaponMP7:
    pass

class C_WeaponMP9:
    pass

class C_WeaponMag7:
    pass

class C_WeaponNOVA:
    pass

class C_WeaponNegev:
    pass

class C_WeaponP250:
    pass

class C_WeaponP90:
    pass

class C_WeaponRevolver:
    pass

class C_WeaponSCAR20:
    pass

class C_WeaponSG556:
    pass

class C_WeaponSSG08:
    pass

class C_WeaponSawedoff:
    pass

class C_WeaponTaser:
    m_fFireTime = 0x1FC0  # unknown_t
    m_nLastAttackTick = 0x1FC4  # unknown_t
    pass

class C_WeaponTec9:
    pass

class C_WeaponUMP45:
    pass

class C_WeaponUSPSilencer:
    pass

class C_WeaponXM1014:
    pass

class C_World:
    pass

class C_WorldModelGloves:
    pass

class C_fogplayerparams_t:
    m_hCtrl = 0x8  # unknown_t
    m_flTransitionTime = 0xC  # unknown_t
    m_OldColor = 0x10  # unknown_t
    m_flOldStart = 0x14  # unknown_t
    m_flOldEnd = 0x18  # unknown_t
    m_flOldMaxDensity = 0x1C  # unknown_t
    m_flOldHDRColorScale = 0x20  # unknown_t
    m_flOldFarZ = 0x24  # unknown_t
    m_NewColor = 0x28  # unknown_t
    m_flNewStart = 0x2C  # unknown_t
    m_flNewEnd = 0x30  # unknown_t
    m_flNewMaxDensity = 0x34  # unknown_t
    m_flNewHDRColorScale = 0x38  # unknown_t
    m_flNewFarZ = 0x3C  # unknown_t
    pass

class CountdownTimer:
    m_duration = 0x8  # unknown_t
    m_timestamp = 0xC  # unknown_t
    m_timescale = 0x10  # unknown_t
    m_nWorldGroupId = 0x14  # unknown_t
    pass

class EngineCountdownTimer:
    m_duration = 0x8  # unknown_t
    m_timestamp = 0xC  # unknown_t
    m_timescale = 0x10  # unknown_t
    pass

class EntityRenderAttribute_t:
    m_ID = 0x30  # unknown_t
    m_Values = 0x34  # unknown_t
    pass

class EntitySpottedState_t:
    m_bSpotted = 0x8  # unknown_t
    m_bSpottedByMask = 0xC  # unknown_t
    pass

class FilterDamageType:
    m_iDamageType = 0x650  # unknown_t
    pass

class FilterHealth:
    m_bAdrenalineActive = 0x650  # unknown_t
    m_iHealthMin = 0x654  # unknown_t
    m_iHealthMax = 0x658  # unknown_t
    pass

class IntervalTimer:
    m_timestamp = 0x8  # unknown_t
    m_nWorldGroupId = 0xC  # unknown_t
    pass

class OutflowWithRequirements_t:
    m_Connection = 0x0  # unknown_t
    m_DestinationFlowNodeID = 0x48  # unknown_t
    m_RequirementNodeIDs = 0x50  # unknown_t
    m_nCursorStateBlockIndex = 0x68  # unknown_t
    pass

class PhysicsRagdollPose_t:
    m_Transforms = 0x8  # unknown_t
    m_hOwner = 0x20  # unknown_t
    m_bSetFromDebugHistory = 0x24  # unknown_t
    pass

class PredictedDamageTag_t:
    nTagTick = 0x30  # unknown_t
    flFlinchModSmall = 0x34  # unknown_t
    flFlinchModLarge = 0x38  # unknown_t
    flFriendlyFireDamageReductionRatio = 0x3C  # unknown_t
    pass

class PulseNodeDynamicOutflows_t:
    m_Outflows = 0x0  # unknown_t
    pass

class PulseNodeDynamicOutflows_t__DynamicOutflow_t:
    m_OutflowID = 0x0  # unknown_t
    m_Connection = 0x8  # unknown_t
    pass

class PulseObservableBoolExpression_t:
    m_EvaluateConnection = 0x0  # unknown_t
    m_DependentObservableVars = 0x48  # unknown_t
    m_DependentObservableBlackboardReferences = 0x60  # unknown_t
    pass

class PulseSelectorOutflowList_t:
    m_Outflows = 0x0  # unknown_t
    pass

class SellbackPurchaseEntry_t:
    m_unDefIdx = 0x30  # unknown_t
    m_nCost = 0x34  # unknown_t
    m_nPrevArmor = 0x38  # unknown_t
    m_bPrevHelmet = 0x3C  # unknown_t
    m_hItem = 0x40  # unknown_t
    pass

class SequenceHistory_t:
    m_hSequence = 0x0  # unknown_t
    m_flSeqStartTime = 0x4  # unknown_t
    m_flSeqFixedCycle = 0x8  # unknown_t
    m_nSeqLoopMode = 0xC  # unknown_t
    m_flPlaybackRate = 0x10  # unknown_t
    m_flCyclesPerSecond = 0x14  # unknown_t
    pass

class SignatureOutflow_Continue:
    pass

class SignatureOutflow_Resume:
    pass

class VPhysicsCollisionAttribute_t:
    m_nInteractsAs = 0x8  # unknown_t
    m_nInteractsWith = 0x10  # unknown_t
    m_nInteractsExclude = 0x18  # unknown_t
    m_nEntityId = 0x20  # unknown_t
    m_nOwnerId = 0x24  # unknown_t
    m_nHierarchyId = 0x28  # unknown_t
    m_nCollisionGroup = 0x2A  # unknown_t
    m_nCollisionFunctionMask = 0x2B  # unknown_t
    pass

class ViewAngleServerChange_t:
    nType = 0x30  # unknown_t
    qAngle = 0x34  # unknown_t
    nIndex = 0x40  # unknown_t
    pass

class WeaponPurchaseCount_t:
    m_nItemDefIndex = 0x30  # unknown_t
    m_nCount = 0x32  # unknown_t
    pass

class WeaponPurchaseTracker_t:
    m_weaponPurchases = 0x8  # unknown_t
    pass

class audioparams_t:
    localSound = 0x8  # unknown_t
    soundscapeIndex = 0x68  # unknown_t
    localBits = 0x6C  # unknown_t
    soundscapeEntityListIndex = 0x70  # unknown_t
    soundEventHash = 0x74  # unknown_t
    pass

class fogparams_t:
    dirPrimary = 0x8  # unknown_t
    colorPrimary = 0x14  # unknown_t
    colorSecondary = 0x18  # unknown_t
    colorPrimaryLerpTo = 0x1C  # unknown_t
    colorSecondaryLerpTo = 0x20  # unknown_t
    start = 0x24  # unknown_t
    end = 0x28  # unknown_t
    farz = 0x2C  # unknown_t
    maxdensity = 0x30  # unknown_t
    exponent = 0x34  # unknown_t
    HDRColorScale = 0x38  # unknown_t
    skyboxFogFactor = 0x3C  # unknown_t
    skyboxFogFactorLerpTo = 0x40  # unknown_t
    startLerpTo = 0x44  # unknown_t
    endLerpTo = 0x48  # unknown_t
    maxdensityLerpTo = 0x4C  # unknown_t
    lerptime = 0x50  # unknown_t
    duration = 0x54  # unknown_t
    blendtobackground = 0x58  # unknown_t
    scattering = 0x5C  # unknown_t
    locallightscale = 0x60  # unknown_t
    enable = 0x64  # unknown_t
    blend = 0x65  # unknown_t
    m_bPadding2 = 0x66  # unknown_t
    m_bPadding = 0x67  # unknown_t
    pass

class shard_model_desc_t:
    m_nModelID = 0x8  # unknown_t
    m_hMaterialBase = 0x10  # unknown_t
    m_hMaterialDamageOverlay = 0x18  # unknown_t
    m_solid = 0x20  # unknown_t
    m_vecPanelSize = 0x24  # unknown_t
    m_vecStressPositionA = 0x2C  # unknown_t
    m_vecStressPositionB = 0x34  # unknown_t
    m_vecPanelVertices = 0x40  # unknown_t
    m_vInitialPanelVertices = 0x58  # unknown_t
    m_flGlassHalfThickness = 0x70  # unknown_t
    m_bHasParent = 0x74  # unknown_t
    m_bParentFrozen = 0x75  # unknown_t
    m_SurfacePropStringToken = 0x78  # unknown_t
    pass

class sky3dparams_t:
    scale = 0x8  # unknown_t
    origin = 0xC  # unknown_t
    bClip3DSkyBoxNearToWorldFar = 0x18  # unknown_t
    flClip3DSkyBoxNearToWorldFarOffset = 0x1C  # unknown_t
    fog = 0x20  # unknown_t
    m_nWorldGroupID = 0x88  # unknown_t
    pass
