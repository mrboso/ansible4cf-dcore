sed -i "
        s/Replace_DcoreImageTag/${DcoreImageTag}/g
        s/Replace_DcoreUserName/${DcoreUserName}/g
        s/Replace_DcoreNetName/${DcoreNetName}/g
        s/Replace_DcoreRPCport/${DcoreRPCport}/g
        s/Replace_DcoreExposeRPCPort/${DcoreExposeRPCPort}/g
        s/Replace_DcoreP2Pport/${DcoreP2Pport}/g
        s/Replace_DcoreAllowNginx/${DcoreAllowNginx}/g
        s/Replace_DcoreRoleCustom/${DcoreRoleCustom}/g
        s/Replace_DcoreRoleCustomName/${DcoreRoleCustomName}/g
        s/Replace_DcoreRoleMiner/${DcoreRoleMiner}/g
        s/Replace_DcoreRoleSeeder/${DcoreRoleSeeder}/g
        s/Replace_DcoreSeedNode/${DcoreSeedNode}/g
        s/Replace_DcoreNginxSslSelfsigned/${DcoreNginxSslSelfsigned}/g
        s/Replace_DcoreNginxSslCN/${DcoreNginxSslCN}/g
        s/Replace_DcoreAllowIPFS/${DcoreAllowIPFS}/g
        s/Replace_DcoreEnableStalProduction/${DcoreEnableStalProduction}/g
        s/Replace_DcoreRequiredMinersParticipation/${DcoreRequiredMinersParticipation}/g
        s/Replace_DcoreMinerID/${DcoreMinerID}/g
        s/Replace_DcoreMinerPrivateKey/${DcoreMinerPrivateKey}/g
        s/Replace_DcoreSeeder/${DcoreSeeder}/g
        s/Replace_DcoreSeederPrivateKey/${DcoreSeederPrivateKey}/g
        s/Replace_DcoreContentPrivateKey/${DcoreContentPrivateKey}/g
        s/Replace_DcoreFreeSpace/${DcoreFreeSpace}/g
        s/Replace_DcoreSeedingPrice/${DcoreSeedingPrice}/g
        s/Replace_DcoreTransactionIDHistory/${DcoreTransactionIDHistory}/g
        s/Replace_DcoreLogLevelDefault/${DcoreLogLevelDefault}/g
        s/Replace_DcoreLogLevelP2P/${DcoreLogLevelP2P}/g
        s/Replace_DcoreLogLevelTransfer/${DcoreLogLevelTransfer}/g
        " $1
