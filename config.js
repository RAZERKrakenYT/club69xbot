module.exports = {
    app: {
        px: '=',
        token: '133e35147aea315dc50d047f89ba44eaeb6b47a628f92274b7265573aa1b4637',
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
