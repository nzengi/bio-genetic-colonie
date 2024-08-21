// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract RobotColony {

    struct Robot {
        address owner;
        uint reputation;
        bool authorized;
    }

    mapping(address => Robot) public robots;
    address public admin;

    constructor() {
        admin = msg.sender;  // The deployer of the contract becomes the admin
    }

    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }

    modifier onlyAuthorized() {
        require(robots[msg.sender].authorized, "Not authorized");
        _;
    }

    // Function to authorize a new robot
    function authorizeRobot(address _robotAddress) external onlyAdmin {
        robots[_robotAddress] = Robot(_robotAddress, 0, true);
    }

    // Function to verify a task and increase reputation
    function verifyTask(address _robotAddress, uint _taskPerformance) external onlyAdmin {
        require(robots[_robotAddress].authorized, "Robot is not authorized");
        robots[_robotAddress].reputation += _taskPerformance;
    }

    // Function to revoke robot authorization
    function revokeAuthorization(address _robotAddress) external onlyAdmin {
        robots[_robotAddress].authorized = false;
    }

    // Function to get a robot's reputation
    function getReputation(address _robotAddress) external view returns (uint) {
        return robots[_robotAddress].reputation;
    }
}
