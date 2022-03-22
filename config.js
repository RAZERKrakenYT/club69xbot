module.exports = {
    app: {
        px: '=',
        token: 'OTU1ODUyMTM0Mjc0OTU3Mzgy.Yjnsqw.yWnhhbNzM5GpzhkptC-nXsG0wVE',
        playing: 'By CLOUDEX™'
    },

    opt: {
        DJ: {
            enabled: false,
            roleName: 'CLOUDEX™',
            commands: ['back', 'clear', 'filter', 'loop', 'pause', 'resume', 'seek', 'shuffle', 'skip', 'stop', 'volume']
        },
        maxVol: 100,
        loopMessage: false,
        discordPlayer: {
            ytdlOptions: {
                quality: 'highestaudio',
                highWaterMark: 1 << 25
            }
        }
    }
};
