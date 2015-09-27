// the semi-colon before function invocation is a safety net against concatenated
// scripts and/or other plugins which may not be closed properly.
;
(function ($, window, document, undefined) {

    var fbComments = 'fbComments',
        defaults = {
            appId: null,
            version: 'v2.4',
            language: 'en_US',
            trigger: 'lazyload',
            threshold: 300,
            gaEnabled: true,
            gaGlobal: null,
            gtmOverride: false,
        };

    function FacebookComments(element, options) {
        this.element = $(element);

        this.universalGA = false;
        this.classicGA = false;

        this.settings = $.extend({}, defaults, options);

        if (this.settings.gaEnabled) {
            if (this.settings.gaGlobal) {
                this.universalGA = true;
                this.gaGlobal = this.settings.gaGlobal;
            } else if (typeof ga === 'function') {
                this.universalGA = true;
                this.gaGlobal = 'ga';
            } else if (typeof __gaTracker === 'function') {
                this.universalGA = true;
                this.gaGlobal = '__gaTracker';
            } else if (typeof _gaq !== 'undefined' && typeof _gaq.push === 'function') {
                this.classicGA = true;
            }
        }


        this._defaults = defaults;
        this._name = fbComments;
        this.init();
    }

    FacebookComments.prototype = {
        init: function () {
            this.getScript();

            this.element.one('appear', function () {
                var commentWrapper = $('js-comments-wrapper', this.element);
                FB.XFBML.parse(commentWrapper[0]);
            }.bind(this));

            this.element.on('fb.sdk.loaded', function () {
                this.bindEvents();

                switch (this.settings.trigger) {
                case 'immediately':
                    this.element.trigger('appear');
                    break;

                case 'lazyload':
                    this.checkIsInViewport();
                    this.onScroll();
                    break;

                case 'click':
                    this.onClick();
                    break;
                }
            }.bind(this));
        },
        debounce: function (func, delay, immediate) {
            var timeout, result;
            return function () {
                var context = this,
                    args = arguments;
                var later = function () {
                    timeout = null;
                    if (!immediate) {
                        result = func.apply(context, args);
                    }
                };
                var callNow = immediate && !timeout;
                clearTimeout(timeout);
                timeout = setTimeout(later, delay);
                if (callNow) {
                    result = func.apply(context, args);
                }
                return result;
            };
        },
        getScript: function () {
            $.ajax({
                url: '//connect.facebook.net/' + this.settings.language + '/sdk.js',
                dataType: 'script',
                cache: true
            }).done(function () {
                FB.init({
                    appId: this.settings.appId,
                    version: this.settings.version,
                    xfbml: false,
                    status: false
                });
                this.element.trigger('fb.sdk.loaded');
            }.bind(this));
        },
        onScroll: function () {
            $(window).on('scroll', this.debounce(function () {
                this.checkIsInViewport();
            }.bind(this), 300));
        },
        checkIsInViewport: function () {
            if ($.inviewport(this.element, { threshold: this.settings.threshold })) {
                this.element.trigger('appear');
            }
        },
        onClick: function () {
            var that = this;
            $('.js-show-comments', this.element).on('click', function () {
                that.element.trigger('appear');
                $(this).fadeOut().remove();
            });
        },
        bindEvents: function () {
            var that = this;
            FB.Event.subscribe('comment.create', function (comment) {
                this.trackEvent('New Comment', comment)
            }.bind(this));
            FB.Event.subscribe('comment.remove', function (comment) {
                this.trackEvent('Remove Comment', comment)
            }.bind(this));
        },
        trackEvent: function (action, comment) {
            if (!this.settings.gaEnabled) {
                return false;
            }

            var trackingData = {
                hitType: 'social',
                socialNetwork: 'Facebook',
                socialTarget: comment.href,
                socialAction: action
            };

            if (typeof dataLayer !== 'undefined' && typeof dataLayer.push === 'function' && !this.settings.gtmOverride) {
                dataLayer.push(trackingData);
            } else if (this.universalGA) {
                window[this.gaGlobal]('send', 'social', {
                    socialNetwork: trackingData.socialNetwork,
                    socialAction: trackingData.socialAction,
                    socialTarget: trackingData.socialTarget
                })
            } else if (this.classicGA) {
                _gaq.push(['_trackSocial', trackingData.socialNetwork, trackingData.socialAction, trackingData.socialTarget]);
            }
        }
    };

    $.fn[fbComments] = function (options) {
        return this.each(function () {
            if (!$.data(this, 'plugin_' + fbComments)) {
                $.data(this, 'plugin_' + fbComments, new FacebookComments(this, options));
            }
        });
    };

})(jQuery, window, document);
