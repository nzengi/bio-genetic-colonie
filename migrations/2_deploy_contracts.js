const RobotColony = artifacts.require("RobotColony");

module.exports = function(deployer) {
  deployer.deploy(RobotColony);
};
