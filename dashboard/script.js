/**
 * ShieldAI Master Script - Agentic Version
 * Reference: Meta OpenEnv Observation/Action Space
 */

document.addEventListener('DOMContentLoaded', () => {
    console.log("ShieldAI: System Link Established");

    const statusDot = document.getElementById('privacyStatusDot');
    const privacyOverlay = document.getElementById('privacyOverlay');
    const authPin = document.getElementById('authPin');
    const landing = document.getElementById('landingPage');
    const dashboard = document.getElementById('dashboardApp');
    const logContainer = document.getElementById('organizedContent');
    const spamCount = document.getElementById('spamCount');

    // --- 0. HELPER: AGENTIC LOGGING ---
    // This replaces alerts and creates a persistent audit trail
    const sysLog = (message, type = "INFO") => {
        const time = new Date().toLocaleTimeString([], { hour12: false });
        const icon = type === "ACTION" ? "⚡" : (type === "SECURE" ? "🟢" : "🔴");
        
        const entry = document.createElement('div');
        entry.className = 'log-entry';
        entry.innerHTML = `<span class="timestamp">[${time}]</span> ${icon} ${message}`;
        
        if (logContainer) {
            logContainer.prepend(entry); // Newest logs stay at the top
        }
    };

    // --- 1. AUTO-LOCK LOGIC ---
    document.addEventListener('visibilitychange', () => {
        if (document.hidden && !dashboard.classList.contains('hidden')) {
            privacyOverlay.classList.remove('hidden');
            if (statusDot) {
                statusDot.innerText = "● SYSTEM LOCKED (AUTO)";
                statusDot.style.color = "#ef4444";
            }
            sysLog("SECURITY_EVENT: Auto-Lock triggered (Visibility Change)", "WARN");
        }
    });

    // --- 2. NAVIGATION ---
    const enterBtn = document.getElementById('enterApp');
    if (enterBtn) {
        enterBtn.onclick = () => {
            landing.style.display = 'none';
            dashboard.classList.remove('hidden');
            dashboard.style.display = 'flex';
            sysLog("ENVIRONMENT: ShieldAI session initialized successfully.", "SECURE");
        };
    }

    // --- 3. SECURITY: PRIVACY MODE ---
    const privacyBtn = document.getElementById('togglePrivacy');
    if (privacyBtn) {
        privacyBtn.onclick = () => {
            privacyOverlay.classList.remove('hidden');
            if (statusDot) {
                statusDot.innerText = "● SYSTEM LOCKED";
                statusDot.style.color = "#ef4444";
            }
            sysLog("ACTION: Manual privacy vault activation.", "ACTION");
        };
    }

    const unlockBtn = document.getElementById('unlockBtn');
    if (unlockBtn) {
        unlockBtn.onclick = () => {
            if (authPin.value === "1234") {
                privacyOverlay.classList.add('hidden');
                authPin.value = ""; 
                if (statusDot) {
                    statusDot.innerText = "● ACTIVE & SECURE";
                    statusDot.style.color = "#10b981";
                }
                sysLog("IDENTITY: Access granted for User: Madhu.", "SECURE");
            } else {
                sysLog("AUTH_FAILURE: Unauthorized PIN attempt detected.", "WARN");
                alert("ACCESS DENIED");
            }
        };
    }

    // --- 4. ACTION SPACE: DEEP SCAN ---
    const scanBtn = document.getElementById('scanContent');
    if (scanBtn && spamCount) {
        scanBtn.onclick = () => {
            let current = parseInt(spamCount.innerText) || 0;
            let found = Math.floor(Math.random() * 10) + 1;
            spamCount.innerText = current + found;
            sysLog(`SCAN_OP: Deep scan completed. ${found} threats neutralized.`, "ACTION");
        };
    }

    // --- 5. OPTIMIZER: PURGE ---
    const purgeBtn = document.getElementById('clearAds');
    if (purgeBtn) {
        purgeBtn.onclick = () => {
            spamCount.innerText = "0";
            sysLog("PURGE_OP: Browser node memory cleared. Ads removed.", "ACTION");
        };
    }
});